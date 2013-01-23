import re
import sublime
import sublime_plugin

class AutoEncodingForRuby(sublime_plugin.EventListener):
  def __init__(self):
    self.settings = sublime.load_settings("Auto Encoding for Ruby.sublime-settings")

  def on_load(self, view):
    self.handle_encoding_declaration_on(view)

  def on_modified(self, view):
    if not self.get_settings("checking_encoding_on_pre_save_only", view):
      self.handle_encoding_declaration_on(view)

  def on_pre_save(self, view):
    if self.get_settings("checking_encoding_on_pre_save_only", view):
      self.handle_encoding_declaration_on(view)

  def handle_encoding_declaration_on(self, view):
    if self.is_allowed_to_generate_encoding_declaration_on_current_syntax(view):
      if self.always_generate_encoding_declaration(view):
        if not self.has_encoding_declaration_on_first_line_of(view):
            self.add_encoding_declaration_on_the_first_line_of(view)
      else:
        try:
          self.decode_to_ascii_the_content_of(view)
        except UnicodeEncodeError:
          if not self.has_encoding_declaration_on_first_line_of(view):
            self.add_encoding_declaration_on_the_first_line_of(view)
        else:
          if self.has_encoding_declaration_on_first_line_of(view):
            self.remove_encoding_declaration_on_the_first_line_of(view)

  def always_generate_encoding_declaration(self, view):
    return self.get_settings("always_generate_encoding_declaration", view)

  def is_allowed_to_generate_encoding_declaration_on_current_syntax(self, view):
    allowed_syntaxes = self.get_settings("allowed_syntaxes", view)
    current_syntax = self.get_settings("syntax", view)

    return current_syntax in allowed_syntaxes

  def get_settings(self, name, view, default = None):
    setting_value = view.settings().get(name, default)

    if setting_value == None:
      setting_value = self.settings.get(name)

    return setting_value

  def decode_to_ascii_the_content_of(self, view):
    self.content_without_comments_of(view).decode("ascii")

  def content_without_comments_of(self, view):
    file_content = view.substr(sublime.Region(0, view.size()))
    content_without_comments = ""

    for line in file_content.split("\n"):
      striped_line = line.strip()

      if not striped_line.startswith("#"):
        content_without_comments += striped_line.rstrip() + "\n"

    return content_without_comments

  def has_encoding_declaration_on_first_line_of(self, view):
    encoding_declaration_regex = self.get_settings("encoding_declaration_regex", view)

    return re.search(encoding_declaration_regex, self.first_line_from(view), re.IGNORECASE)

  def first_line_from(self, view):
    return view.substr(view.full_line(0))

  def add_encoding_declaration_on_the_first_line_of(self, view):
    edit = view.begin_edit()
    encoding_declaration = self.get_settings("encoding_declaration", view)
    view.insert(edit, 0, encoding_declaration)
    view.end_edit(edit)

  def remove_encoding_declaration_on_the_first_line_of(self, view):
    if not self.get_settings("remove_encoding_declaration", view):
      return

    edit = view.begin_edit()
    self.erase_first_line_of(view, edit)

    if self.has_only_whitespace_on_the_first_line_of(view):
      self.erase_first_line_of(view, edit)

    view.end_edit(edit)

  def erase_first_line_of(self, view, edit):
    view.erase(edit, view.full_line(0))

  def has_only_whitespace_on_the_first_line_of(self, view):
    return re.search("^\s*$", self.first_line_from(view))
