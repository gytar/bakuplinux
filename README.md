# Backup 


This is a simple backup python program for <em>normally</em> all linux distributions (works on Fedora 33 so far). 

You can choose a device on which you want to put your data as such 

```
user@os:~$ python3 backup.py -c
You are about to change origin and destination paths: 
Continue? (y/n): y
Your actual origin path is: /home/user
Your actual destination path is: /run/media/user/usb-whatever

Where do you want to back up ?
    1) USB drive (media/...)
    2) Somewhere else
    3) Set default
Input choice: 1

Here are all your devices | their path:
    1) [USB_NAME] | /path/to/usb/device
    2) [USB_NAME] | /path/to/usb/device
Which one will you choose ? 
```

And it will do your backup simply by executing the script with `python3 backup.py` in the terminal.

## Commands

backup [COMMANDS]
or
python3 /path/to/file/backup.py [COMMANDS]

    --choose  / -c  => to change the destination folder or device
    --help    / -h  => display this help message
    --version / -v  => show version
    --show    / -s  => show [DESTINATION] then [ORIGIN] directories

default ORIGIN directory: /home/[USER]

default DESTINATION directoty: NONE


## TODO

Create an alias in your ~/.bashrc or ~/.bash_aliases file 
