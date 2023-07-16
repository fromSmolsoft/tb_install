# Thunderbird automated tar install

Automatically download and install thunderbird from tar.

# Usage

1. Open your favorite terminal, usually `ctrl + atl + T`
2. Make sure open the terminal opened at this project location. Something like
   this `user@computer:~/.../ThunderbirdInstall/thunderbird_install$ ` . If it's not:
    - either use `cd ~/.../ThunderbirdInstall/`  replace `...` with path to where you safed folder or
    - use your preferred file explorer to go project folder and open the terminal there usually by clicking `RMB`
      🖰  `>` `open in terminal`.
3. Run `python3 linux64_tar.py`
4. Wait and enter your `[sudo] password for user: ` when promted

# Use at your own risk !

Uses standard terminal commands like `mv` and doesn't clear terminal. It can be seen what is happening during a script
run.   
All used terminal commands can be found in corresponding `*.py` file. I try to keep it short and readable.  
Tested on _Linux Mint 21.1 Vera base: Ubuntu 22.04 jammy, Python 3.10.6_.  
It should work on ubuntu based distros.

# How it works

1. Tool downloads tar from Thunderbird's download link specified in `config.ini` to `download_path`.
2. Extracts `*.tar` archive
3. Checks for existing `Thunderbird` folder already located at `opt_path`
    - if `Thunderbird exists` it will move existing folder to the `Thunderbird_backu` folder and proceed.
4. Moves the uncompressed Thunderbird folder `opt_path`
5. Creates a symlink to the Thunderbird executable
6. Check if the desktop file has been installed using this script before
    - if yes, Move the current desktop file to a backup folder
7. Download an official Thunderbird copy of the desktop file and puts it into `applications_path`

## Default [links]

~~`thunderbird_latest` = https://download.mozilla.org/?product=thunderbird-latest&os=linux64&lang=en-US~~ ← Currently
not pointing to the latest stable release.

`thunderbird_latest` = https://download-installer.cdn.mozilla.net/pub/thunderbird/releases/115.0/linux-x86_64/en-US/thunderbird-115.0.tar.bz2  
`desktop_file` = https://raw.githubusercontent.com/mozilla/sumo-kb/main/installing-thunderbird-linux/thunderbird.desktop

## Default [paths]

`download_path` = ~/Downloads  
`opt_path` = /opt  
`bin_path` = /usr/local/bin  
`applications_path` = /usr/local/share/applications

# Requirements

Python 3.X.X (Often preinstalled on many distros).

# Roadmap

- [x] automate installation of TB 115 from `*.tar`.
- [ ] uninstall script
- [ ] one script to rule them all