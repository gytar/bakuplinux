#!/usr/bin/env python

import os
import sys
import getpass

folders=""
backup_path=""
backup="backup.tar.gz"
home= "/home/" + getpass.getuser()


usb_file = "usb.conf"
usb_names = []
 
def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        elif reply[0] == 'n':
            return False
        else:
        	print("the answer is invalid")

def help():
    os.system(f'cat {home}/backup/help.txt')

def version():
    os.system(f'cat {home}/backup/version.txt')

def show_data():
    with open(f"{home}/backup/backupdata.conf", "r") as f:
        print("Destination directory: ", end='')
        print(f.readline(), end="")
        print("Origin directory: ", end='')
        print(f.readline())
        

def search_usb(): 
    global usb_file, home, usb_names
    # requete pour avoir les chemins des clés  usb
    usb_query = "df -h 2> /dev/null | awk '{for(i=6; i<=NF;++i)printf $i\"\"FS; print \"\"}' | awk '/media/ {print $0}'"
    
    
    f = open(f"{home}/backup/{usb_file}", 'w+')

    os.system(f"{usb_query} >> {home}/backup/{usb_file}")
    
    all_usbs = f.read()
    all_usbs = str.split(all_usbs, ' \n')
    all_usbs = [string for string in all_usbs if string != ""]
    f.close()
    for i in range(len(all_usbs)):
        an_array = all_usbs[i].split("/")
        usb_names.append(an_array[-1])
        # all_usbs[i] = all_usbs[i].replace(" ", "\ ")
    
    return all_usbs
    

def search_values(): 
    global folders, backup_path, home
    
    f = open(f"{home}/backup/backupdata.conf", 'r')
    data = f.read()
    f.close
    if os.path.getsize(f'{home}/backup/backupdata.conf') == 0:
        f = open(f'{home}/backup/backupdata.conf', 'a') 
        backup_path="NONE"
        folders=home
        f.close()
    else: 
        data = str.split(data, "\n")
        backup_path=data[0]
        folders=data[1]

def change(): 
    global folders, backup_path, usb_names

    fake_backup = backup_path
    fake_folders = folders
    usb_paths = search_usb()

    
    f = open(f"{home}/backup/backupdata.conf", "w+")
    
    print("You are about to change origin and destination paths: ")
    if yes_or_no("Continue?"):
        print(f'Your actual origin path is: {folders}')
        print(f'Your actual destination path is: {backup_path}')
        print('')
        print('Where do you want to back up ?')
        print('    1) USB drive (media/...)')
        print('    2) Somewhere else')
        print('    3) Set default')
        choice = input("Input choice: ")
        print('')
        if int(choice) == 1 or int(choice == ""):
            if(len(usb_names) >= 1):
                print("Here are all your devices:")
                for i in range(len(usb_names)):
                    dis_choice = i+1
                    print(f'    {dis_choice}) {usb_names[i]}')

                choice = int(input("Which one will you choose ? ")) - 1
                backup_path = usb_paths[choice]
                print("")
                if yes_or_no(f"you have chosen {usb_names[choice]}, are you sure ?"):
                    datatowrite = str(backup_path) + "\n" + str(folders)
                    f.write(datatowrite)
                    f.close()
                else:
                    print("ok, i do nothing")
                    print("bye")
                folders = input('Enter the new origin: (enter to pass)')
                if not folders: 
                    folders = fake_folders
                
            else:
                print("there are no devices connected")
                print("plug a device and restart the program")
                sys.exit(0)
        elif int(choice) == 2: 
            backup_path = input('Enter the new reciever: (enter to pass)')
            if not backup_path:
                backup_path = fake_backup
            folders = input('Enter the new origin: (enter to pass)')
            if not folders: 
                folders = fake_folders
        elif int(choice) == 3: 
            backup_path="NONE"
            folders=home
            datatowrite = str(backup_path) + "\n" + str(folders)
            f.write(datatowrite)
            f.close()
            
    else:
        print("Ok bye")

    print("Changes accepted")
    print(f"New origin folder: {folders}")
    print(f"New destination folder: {backup_path}")


def backingup():
    print(home)
    print("You're about to do a backup")
    if yes_or_no("Continue?"): 
        if os.path.exists(f'{backup_path}'):
            os.system("echo 'backup in progress'")
            if os.path.exists(f'{backup_path}/{backup}'):
                os.system(f'rm -r {backup_path}/{backup}')
            else: 
                os.system(f'tar -cvzf {backup} {folders}')
                os.system(f'mv {backup} {backup_path}')
            os.system("echo 'backup done!'")
        else:
            os.system('echo "error: USB not plugged or backup path not found"')
            os.system(f'echo "path {backup_path} not found"')
    else:
        print("ok bye")

def main():
    search_values()
    if len(sys.argv) == 1:
        backingup()
        sys.exit(0)        
    elif len(sys.argv) == 2: 
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            help()
            sys.exit(0)
        elif sys.argv[1] == "-c" or sys.argv[1] == "--choose":
            change()
            sys.exit(0)
        elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
            version()
            sys.exit(0)
        elif sys.argv[1] == "--show" or sys.argv[1] == "-s":
            show_data()
            sys.exit(0)

if __name__ == '__main__':
    main()