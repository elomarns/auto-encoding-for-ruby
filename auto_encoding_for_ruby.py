import re
import sublime
import sublime_plugin

class AutoEncodingForRuby(sublime_plugin.EventListener):
  def on_load(self, view):
    self.handle_encoding_declaration_on(view)

  def on_modified(self, view):
    self.handle_encoding_declaration_on(view)

  def handle_encoding_declaration_on(self, view):
    if self.is_allowed_to_generate_encoding_declaration_on_current_syntax(view):
      try:
        self.decode_to_ascii_the_content_of(view)
      except UnicodeEncodeError:
        if not self.has_encoding_declaration_on_first_line_of(view):
          self.add_encoding_declaration_on_the_first_line_of(view)
      else:
        if self.has_encoding_declaration_on_first_line_of(view):
          self.remove_encoding_declaration_on_the_first_line_of(view)

  def is_allowed_to_generate_encoding_declaration_on_current_syntax(self, view):
    allowed_syntaxes = view.settings().get("allowed_syntaxes")
    current_syntax = view.settings().get("syntax")

    return current_syntax in allowed_syntaxes

  def decode_to_ascii_the_content_of(self, view):
    file_content = view.substr(sublime.Region(0, view.size()))

    file_content.decode("ascii")

  def has_encoding_declaration_on_first_line_of(self, view):
    return re.search("^\s*#\s*encoding\s*:\s*utf-8\s*$", self.first_line_from(view), re.IGNORECASE)

  def first_line_from(self, view):
    return view.substr(view.full_line(0))

  def add_encoding_declaration_on_the_first_line_of(self, view):
    edit = view.begin_edit()
    view.insert(edit, 0, "#encoding: utf-8\n\n")
    view.end_edit(edit)

  def remove_encoding_declaration_on_the_first_line_of(self, view):
    edit = view.begin_edit()
    self.erase_first_line_of(view, edit)

    if self.has_only_whitespace_on_the_first_line_of(view):
      self.erase_first_line_of(view, edit)

    view.end_edit(edit)

  def erase_first_line_of(self, view, edit):
    view.erase(edit, view.full_line(0))

  def has_only_whitespace_on_the_first_line_of(self, view):
    return re.search("^\s*$", self.first_line_from(view))