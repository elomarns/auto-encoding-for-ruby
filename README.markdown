# Auto Encoding for Ruby

I hate the need to include #encoding: utf-8 on every Ruby file with non-ASCII characters. So I've created this plugin to save me from this boring task. It automatically adds an encoding declaration on the top of Ruby files when needed, and remove it when it's not necessary anymore. Simple as that.

## Installation

You have 3 options for installing Auto Encoding for Ruby: using Package Control, using Git, or just downloading it.

### Package Control

Inside Sublime Text 2, open your command pallete (⌘ + ⇧ + P on OS X), and select "Package Control: Install Package". After this, search for "Auto Encoding for Ruby" and install it!

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

## Licensing

You're free to do whatever you want with this plugin. How about this as a license?