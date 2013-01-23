# Auto Encoding for Ruby

I hate the need to include `# encoding: utf-8` on every Ruby file with non-ASCII characters. So I've created this plugin to save me from this boring task. It automatically adds an encoding declaration on the top of Ruby files when needed, and remove it when it's not necessary anymore. Simple as that.

## Installation

You have 3 options for installing Auto Encoding for Ruby: using Package Control, using Git, or just downloading it.

### Package Control

Inside Sublime Text 2, open your command pallete (`⌘ + ⇧ + P` on OS X), and select `"Package Control: Install Package"`. After this, search for `"Auto Encoding for Ruby"` and install it!

### Git

Open your terminal application and go to your Packages directory, whose location depends on your operating system:

* OS X:

    ```shell
    cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
    ```

* Linux:

    ```shell
    cd ~/.Sublime\ Text 2/Packages/
    ```

* Windows:

    ```shell
    cd %APPDATA%/Sublime Text 2/Packages/
    ```

After this, you just need to clone this repository:

```shell
git clone git://github.com/elomarns/auto-encoding-for-ruby.git "Auto Encoding for Ruby"
```

### Downloading

Click on the nice cloud icon above, and download the zip file containing this plugin. Then unzip the file and move the resulting folder to your Packages directory.

## How to Use

Auto Encoding for Ruby will add an encoding declaration on top of Ruby files on these situations:

* Just after you type the first non-ASCII character of the file;
* When you open a file with non-ASCII characters and no encoding declaration.

It will also remove the encoding declaration on the following cases:

* Just after you delete the last non-ASCII character;
* When you open a file with an encoding declaration but without non-ASCII characters.

In other words, just write your code as you would without the plugin and you'll be fine.

## Configuration

Although this plugin works out of the box, you can tweak it to your needs. Just for reference, this is the default settings, located on `Packages/Auto Encoding for Ruby/Auto Encoding for Ruby.sublime-settings` file:

```json
{
  "allowed_syntaxes":
  [
    "Packages/Ruby/Ruby.tmLanguage",
    "Packages/Rails/Ruby on Rails.tmLanguage",
    "Packages/RSpec/RSpec.tmLanguage"
  ],

  "encoding_declaration": "# encoding: utf-8\n\n",
  "encoding_declaration_regex": "^\\s*#\\s*encoding\\s*:\\s*utf-8\\s*$",
  "remove_encoding_declaration": true,
  "checking_encoding_on_pre_save_only": false
}
```

### Allowed Syntaxes

By default, Auto Encoding for Ruby will works with Ruby, Ruby on Rails and RSpec syntaxes. But you can add or remove syntaxes by setting a new value on `"allowed_syntaxes"`, on your `Packages/User/Auto Encoding for Ruby.sublime-settings` file. For example, if you want to remove the RSpec support, just update this setting to this:

```json
{
  "allowed_syntaxes":
  [
    "Packages/Ruby/Ruby.tmLanguage",
    "Packages/Rails/Ruby on Rails.tmLanguage"
  ]
}
```

### Encoding Declaration

The default encoding declaration is `# encoding: #utf-8`, but you can change it if you want. To do this, just set a new value to `"encoding_declaration"` setting on your `Packages/User/Auto Encoding for Ruby.sublime-settings` file. But if you change this setting, you must change `"encoding_declaration_regex"` too. This setting is used to check if your file already has an encoding declaration. So if you change only the encoding declaration but don't update the regex, the plugin won't be able to know if your file already has an encoding declaration, and it will add it infinitely.

This is an example of a changing in this setting:

```json
{
  "encoding_declaration": "# -*- encoding : utf-8 -*-\n\n",
  "encoding_declaration_regex": "^\\s*#\\s*-\\*-\\s*encoding\\s*:\\s*utf-8\\s*-\\*-\\s*$",
  "remove_encoding_declaration": false,
  "checking_encoding_on_pre_save_only": true
}
```

Don't forget to escape character classes on `"encoding_declaration_regex"` setting.

### Always add encoding declaration

By default, this plug in only will add the encoding declaration to the file if it detects a non-ASCII character. If you want to always add the encoding declaration regardless of whether there is a non-ASCII character or not then you change the setting `"always_generate_encoding_declaration"` to `true`.
## Licensing

You're free to do whatever you want with this plugin. How about this as a license?
