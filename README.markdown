# Auto Encoding for Ruby

I hate the need to include #encoding: utf-8 on every Ruby file with non-ASCII characters. So I've created this plugin to save me from this boring task. It automatically adds an encoding declaration on the top of Ruby files when needed, and remove it when it's not necessary anymore. Simple as that.

## Installation

You have 2 options for installing Auto Encoding for Ruby: with or without Git.

### With Git

Open your terminal application and go to your Packages directory, whose location depends on your operating system:

* OS X:

    ```shell
    $ cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
    ```

* Linux:

    ```shell
    $ cd ~/.Sublime\ Text 2/Packages/
    ```

* Windows:

    ```shell
    $ cd %APPDATA%/Sublime Text 2/Packages/
    ```

After this, you just need to clone this repository:

```shell
$ git clone git://github.com/elomarns/auto-encoding-for-ruby.git "Auto Encoding for Ruby"
```

### Without Git

Click on the nice cloud icon above, and download the zip file containing this plugin. Then, unzip the file and move the resulting folder to your Packages directory.

## How to Use

Just write your code, as you would without the plugin. So just after you type the first non-ASCII character on any Ruby file, the plugin will automaticaly adds a #encoding: utf-8 declaration on the top of the file. The opposite is also true: it will remove the encoding declaration when you delete the last non-ASCII character. So, as I've said, just write your code and let the plugin make its work.

## Licensing

You're free to do whatever you want with this plugin.