import os
import sys
import time
import requests
import subprocess
import string
from datetime import datetime, timedelta
import base64
import shutil
import msvcrt
import socket
import keyboard
import random
import zipfile

BRIGHT_BLACK = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
BRIGHT_WHITE = '\033[97m'
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'
BASE_DIR = r"C:\FMOS"

helphelp = f'''
{GREEN}help commands{RESET}
{GREEN}help system{RESET}
{GREEN}help root{RESET}
{GREEN}help devmode{RESET}
'''

systemlist = r'''
usr
- usr\Desktop
- usr\Docs
- usr\Downloads
System
- System\boot
- System\security
- System\security\root
- System\sys
- System\temp
- System\trash
Programms
- Programms\fak
- Programms\sys
'''

helproot = f'''
{BLUE}Help: Root{RESET}

{GREEN}What can you do with root?{RESET}
{BRIGHT_GREEN}connect to FMOS system folders{RESET}
{BRIGHT_GREEN}delete edit view and create files and folders in FMOS system folders{RESET}
{BRIGHT_GREEN}enable developer mode (type help dev){RESET}
'''

helpdev = f'''
{BLUE}Help: Dev Mode{RESET}

{GREEN}What can you do with dev mode?{RESET}
{BRIGHT_GREEN}run python files{RESET}
{BRIGHT_GREEN}requires root to activate and deactivate{RESET}

{YELLOW}How do i activate and deactivate developer mode?{RESET}
{BRIGHT_YELLOW}you can find that if u type help commands{RESET}
'''

commandlist = f'''Commands:

{BLUE}shutdown:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}shutdown{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}shutsdown fmos{RESET}

{BLUE}clear:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}clear{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}clears screen{RESET}

{BLUE}cd:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}cd *foldername{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}connects to a folder in current folder{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}cd foldername\foldername{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}connects to a folder with path{RESET}

{BLUE}dir:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}dir{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}lists all files and folders in current folder{RESET}

{BLUE}rmfile:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}rmfile *file.txt{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}deletes file in current folder{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}rmfile usr\Desktop\file.txt{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}deletes file in path{RESET}

{BLUE}rmdir:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}rmdir *folder{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}deletes folder in current folder{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}rmdir usr\Desktop\folder{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}deletes folder in path{RESET}

{BLUE}note:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}note *file.txt{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}creates file in current folder and opens it in editor{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}rmfile usr\Desktop\file.txt{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}creates file in path and opens it in editor{RESET}

{BLUE}whoami:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}whoami{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}shows your username and if your rooted or if your user{RESET}

{BLUE}say:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}say hello world{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}says whatever you want{RESET}

{BLUE}viewfile:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}viewfile file.txt{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}shows the content of a file in current folder{RESET}

{BLUE}mydir:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}mydir{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}shows what folder you are connected to{RESET}

{BLUE}mkdir:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}mkdir *folder{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}creates folder in current folder{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}mkdir usr\Desktop\folder{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}creates folder in path{RESET}

{BLUE}curl:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}curl example.com{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}Transfers data from or to a server{RESET}

{BLUE}fak install:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}fak install name{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}installes an app or package{RESET}

{BLUE}fak list:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}fak list{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}lists all installed apps or packages{RESET}

{BLUE}fak remove:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}fak remove name{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}removes an app or package{RESET}

{BLUE}fak run:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}fak run name{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}runs an app or package{RESET}

{BLUE}fak online:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}fak online{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}lists all apps or packages that you can download{RESET}

{BLUE}help:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}help commands{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}help with commands{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}help system{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}help lists the default file system{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}help root{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}helps with root{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}help devmode{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}helps with devmode{RESET}

{BLUE}devmode:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}devmode on{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}activates devmode{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}devmode off{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}activates devmode{RESET}

{BLUE}run:{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}run py *main.py{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}runs python script in current folder{RESET}
{GREEN}usage:{RESET} {BRIGHT_GREEN}run py usr\folder\main.py{RESET}
{YELLOW}manual:{RESET} {BRIGHT_YELLOW}runs python script in specified folder{RESET}
'''

def bootlogo():
    logo = f''' {RED} ______ __  __  ____   _____ 
 |  ____|  \\/  |/ __ \\ / ____|
 | |__  | \  / | |  | | (___  
 |  __| | |\/| | |  | |\___ \ 
 | |    | |  | | |__| |____) |
 |_|    |_|  |_|\\____/|_____/ {RESET}'''
    os.system("cls")
    print(logo)
    print()
    print()
def fmosmainmenu():
    bootlogo()
    print()
    print()
    check_wifi_status()
    print()
    print(f"{YELLOW}Need help with commands? then type help commands{RESET}")
    print()
    print()
    rootdir = r"C:\FMOS\usr"
    os.chdir(rootdir)
    while True:
        command = input(f"{BRIGHT_GREEN}~{RESET}$: ")
        
        if command == "shutdown":
            shutdown()
        elif command == "clear":
            os.system("cls")
        elif command.startswith("cd "):
            change_directory(command)
        elif command == "dir":
            list_directory()
        elif command.startswith("rmfile "):
            rmfile(command)
        elif command.startswith("rmdir "):
            rmdir(command)
        elif command.startswith("note "):
            note_command(command)
        elif command == "whoami":
            whoami()
        elif command.startswith("say "):
            say(command)
        elif command.startswith("viewfile "):
            viewfile(command)
        elif command == "mydir":
            mydir()
        elif command.startswith("mkdir "):
            mkdir(command)
        elif command.startswith("curl "):
            curl(command)
        elif command.startswith("fak install "):
            fakinstall(command)
        elif command == "fak list":
            faklist()
        elif command.startswith("fak remove "):
            fakremove(command)
        elif command.startswith("fak run "):
            fakrun(command)
        elif command == "fak online":
            faklistall()
        elif command.startswith("help "):
            help(command)
        elif command.startswith("run py "):
            runpy(command)
        elif command == "devmode on":
            devmode_on()
        elif command == "devmode off":
            devmode_off()
        else:
            print(f"{RED}Command not recognized!{RESET}")
            
def whoami():
    user_file_path = r'C:\FMOS\System\sys\usr'
    if os.path.exists(user_file_path):
        with open(user_file_path, 'r') as file:
            user_name = file.read().strip()
    else:
        user_name = "ERROR"
    
    if is_rooted():
        print(f"root@{user_name}")
    else:
        print(f"user@{user_name}")

def say(command):
    message = command[4:].strip()
    print(message)
    
def curl(command):
    link = command[4:].strip()
    os.system(f"curl {link}")
    
def press_f11():
    keyboard.press_and_release('f11')

def viewfile(command):
    try:
        filename = command[8:].strip()
        final_path = resolve_path(filename)
        if not final_path:
            return
        
        if os.path.isfile(final_path):
            with open(final_path, 'r') as file:
                content = file.read()
                print(content)
        else:
            print(f"{BRIGHT_RED}Error: File not found!{RESET}")
    except Exception as e:
        print(f"{BRIGHT_RED}Error: {str(e)}{RESET}")

def mydir():
    current_dir = os.getcwd()
    relative_path = os.path.relpath(current_dir, BASE_DIR)
    if relative_path.startswith('..'):
        print(f"{BRIGHT_RED}Error: Outside of C:\\FMOS directory!{RESET}")
    else:
        print(relative_path)

def mkdir(command):
    try:
        dirpath = command[6:].strip()
        if dirpath.startswith('*'):
            final_path = os.path.join(os.getcwd(), dirpath[1:])
        else:
            final_path = resolve_path(dirpath)
            if not final_path:
                return
        
        if not os.path.exists(final_path):
            os.makedirs(final_path)
            print(f"{GREEN}Directory created: {final_path}{RESET}")
        else:
            print(f"{BRIGHT_RED}Error: Directory already exists!{RESET}")
    except Exception as e:
        print(f"{BRIGHT_RED}Error: {str(e)}{RESET}")
          
def is_rooted():
    root_file = os.path.join(BASE_DIR, r"System\security\root\rootuser")
    return os.path.isfile(root_file)
    
def is_devmode():
    devfile = os.path.join(BASE_DIR, r"System\security\devusr")
    return os.path.isfile(devfile)
    
def devmode_on():
    if is_rooted():
        devpath = r"System\security\devusr"
        devfile = os.path.join(BASE_DIR, devpath)
        try:
            os.makedirs(os.path.dirname(devfile), exist_ok=True)
            
            with open(devfile, "w") as f:
                f.write(" ")
            print("Developer mode enabled.")
        except Exception as e:
            print(f"{BRIGHT_RED}ERROR: Failed to enable developer mode! {e}{RESET}")
    else:
        print(f"{BRIGHT_RED}ERROR: You are not rooted! You need to be rooted to access developer mode!{RESET}")
        return


def devmode_off():
    if is_rooted():
        devpath = r"System\security\devusr"
        devfile = os.path.join(BASE_DIR, devpath)
        try:
            if os.path.exists(devfile):
                os.remove(devfile)
                print("Developer mode disabled.")
            else:
                print(f"{BRIGHT_RED}ERROR: Developer mode is not enabled!{RESET}")
        except Exception as e:
            print(f"{BRIGHT_RED}ERROR: Failed to disable developer mode! {e}{RESET}")
    else:
        print(f"{BRIGHT_RED}ERROR: You are not rooted! You need to be rooted to access developer mode!{RESET}")
        return
    
def check_password():
    password_file = os.path.join(BASE_DIR, r"System\security\rootpass.md")
    try:
        with open(password_file, 'r') as file:
            encoded_password = file.read().strip()
        stored_password = base64.b64decode(encoded_password).decode('utf-8')
    except FileNotFoundError:
        print(f"{BRIGHT_RED}Error: Password file not found!{RESET}")
        return False

    user_password = input(f"{BRIGHT_YELLOW}Enter password to proceed: {RESET}")
    if user_password == stored_password:
        return True
    else:
        print(f"{BRIGHT_RED}Error: Incorrect password!{RESET}")
        return False
        
def resolve_path(relative_path):
    relative_path = relative_path.strip()
    if relative_path.startswith('*'):
        # Entferne das '*' und speichere relativ zum aktuellen Arbeitsverzeichnis
        final_path = os.path.join(os.getcwd(), relative_path[1:])
    else:
        final_path = os.path.join(BASE_DIR, relative_path)
        if not final_path.startswith(BASE_DIR):
            print(f"{BRIGHT_RED}Error: Access outside of C:\\FMOS is not allowed!{RESET}")
            return None
    return final_path

def rmfile(command):
    try:
        filepath = command[7:].strip()
        final_path = resolve_path(filepath)
        if not final_path:
            return

        if os.path.isfile(final_path):
            print(f"{RED}Do you really want to delete {final_path}? [Y / N] {RESET}")
            yn = input(f"{BRIGHT_GREEN}~{RESET}$: ")
            if yn == "Y":
                sensitive_dirs = ['System', 'System\\security', 'System\\temp', 'System\\trash', 'System\\sys', 'System\\boot', 'Programms\\sys']
                if any(final_path.startswith(os.path.join(BASE_DIR, sensitive_dir)) for sensitive_dir in sensitive_dirs):
                    if not is_rooted():
                        print(f"{BRIGHT_RED}ERROR: You are not rooted!{RESET}")
                        return
                    if not check_password():
                        return
                
                os.remove(final_path)
                print(f"{GREEN}File {final_path} has been deleted.{RESET}")
            elif yn == "N":
                print(f"{YELLOW}File deletion aborted.{RESET}")
            else:
                print(f"{RED}Invalid Option{RESET}")
        else:
            print(f"{BRIGHT_RED}Error: File not found!{RESET}")
    except Exception as e:
        print(f"{BRIGHT_RED}Error: {str(e)}{RESET}")

def rmdir(command):
    try:
        dirpath = command[6:].strip()
        final_path = resolve_path(dirpath)
        if not final_path:
            return

        if os.path.isdir(final_path):
            print(f"{RED}Do you really want to delete directory {final_path}? [Y / N] {RESET}")
            yn = input(f"{BRIGHT_GREEN}~{RESET}$: ")
            if yn == "Y":
                sensitive_dirs = ['System', 'System\\security', 'System\\temp', 'System\\trash', 'System\\sys', 'System\\boot', 'Programms\\sys']
                if any(final_path.startswith(os.path.join(BASE_DIR, sensitive_dir)) for sensitive_dir in sensitive_dirs):
                    if not is_rooted():
                        print(f"{BRIGHT_RED}ERROR: You are not rooted!{RESET}")
                        return
                    if not check_password():
                        return

                shutil.rmtree(final_path)
                print(f"{GREEN}Directory {final_path} and its contents have been deleted.{RESET}")
            elif yn == "N":
                print(f"{YELLOW}Directory deletion aborted.{RESET}")
            else:
                print(f"{RED}Invalid Option{RESET}")
        else:
            print(f"{BRIGHT_RED}Error: Directory not found!{RESET}")
    except Exception as e:
        print(f"{BRIGHT_RED}Error: {str(e)}{RESET}")
        
def shutdown():
    print(f"{RED}Do you realy want to shutdown the system? [Y / N] {RESET}")
    yn = input(f"{BRIGHT_GREEN}~{RESET}$: ")
    if yn == "Y":
        exit()
    elif yn == "N":
        fmosmainmenu()
    else:
        print(f"{RED}Invalid Option{RESET}")
        fmosmainmenu()
        
def change_directory(command):
    try:
        path = command[3:].strip()
        if not path:
            print(f"{BRIGHT_RED}No directory specified!{RESET}")
            return
        
        final_path = resolve_path(path)
        if not final_path:
            return

        if os.path.isdir(final_path):
            sensitive_dirs = ['System', 'System\\security', 'System\\temp', 'System\\trash', 'System\\sys', 'System\\boot', 'Programms\\sys']
            if any(final_path.startswith(os.path.join(BASE_DIR, sensitive_dir)) for sensitive_dir in sensitive_dirs):
                if not is_rooted():
                    print(f"{BRIGHT_RED}ERROR: You are not rooted and cannot access this directory!{RESET}")
                    return

            os.chdir(final_path)
            print(f"{BRIGHT_CYAN}Directory changed to: {path}{RESET}")
        else:
            print(f"{BRIGHT_RED}Error: Directory not found!{RESET}")
    except Exception as e:
        print(f"{BRIGHT_RED}Error: {str(e)}{RESET}")

def save_note(filepath, content):
    try:
        sensitive_dirs = ['System', 'System\\security', 'System\\temp', 'System\\trash', 'System\\sys', 'System\\boot', 'Programms\\sys', 'Programms\\fak']
        if any(filepath.startswith(os.path.join(BASE_DIR, sensitive_dir)) for sensitive_dir in sensitive_dirs):
            if not is_rooted():
                print(f"{BRIGHT_RED}ERROR: You are not rooted and cannot save to this directory!{RESET}")
                return

        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(filepath, 'w') as file:
            file.write(content)
        print(f"{BRIGHT_GREEN}Note saved to {filepath}{RESET}")
    except Exception as e:
        print(f"{BRIGHT_RED}Error: {str(e)}{RESET}")

def note_command(command):
    try:
        parts = command[5:].strip().split(' ', 1)
        if len(parts) == 0:
            print(f"{BRIGHT_RED}Error: No file path or name provided!{RESET}")
            return

        file_path = parts[0]
        if len(parts) > 1:
            initial_text = parts[1]
        else:
            initial_text = ""

        if file_path.startswith('*'):
            final_path = os.path.join(os.getcwd(), file_path[1:])
        else:
            final_path = os.path.abspath(os.path.join(BASE_DIR, file_path))

        # Eingabe der Notiz
        print(f"{GREEN}FILE EDITOR{RESET}")
        print()
        print(f"{RED}Type your note (Ctrl+A to abort, Ctrl+S to save):{RESET}")
        note_lines = [initial_text] if initial_text else ['']  # Initialisiere mit einer leeren Zeile, wenn kein Text vorhanden ist
        while True:
            ch = msvcrt.getch()  # Lese einen einzelnen Tastendruck

            if ch == b'\x03':  # Ctrl+C zum Abbrechen
                print(f"\n{YELLOW}Note entry aborted.{RESET}")
                return
            elif ch == b'\x01':  # Ctrl+A zum Beenden der Eingabe
                print(f"\n{YELLOW}Note entry aborted.{RESET}")
                return
            elif ch == b'\x13':  # Ctrl+S zum Speichern
                save_note(final_path, '\n'.join(note_lines))
                print(f"\n{BRIGHT_GREEN}Note saved to {final_path}{RESET}")
                return
            elif ch == b'\r':  # Enter
                note_lines.append('')  # Neue Zeile hinzufügen
                print()
            elif ch == b'\x08':  # Backspace
                if note_lines and note_lines[-1]:
                    note_lines[-1] = note_lines[-1][:-1]
                    print('\b \b', end='', flush=True)
            else:
                if note_lines:
                    note_lines[-1] += ch.decode()
                    print(ch.decode(), end='', flush=True)
                else:
                    # Falls `note_lines` leer ist, füge eine neue Zeile hinzu und füge dann das Zeichen hinzu
                    note_lines.append(ch.decode())

    except Exception as e:
        print(f"{BRIGHT_RED}Error: {str(e)}{RESET}")

def list_directory():
    current_dir = os.getcwd()
    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)
        if os.path.isdir(item_path):
            print("________________________________________________________________")
            print(f"{BRIGHT_BLUE}{item}{RESET} {BRIGHT_MAGENTA}<dir>{RESET}")
            print("________________________________________________________________")
        else:
            if item.endswith('.txt'):
                print("________________________________________________________________")
                print(f"{GREEN}{item}{RESET} {BRIGHT_MAGENTA}<file text>{RESET}")
                print("________________________________________________________________")
            elif item.endswith('.py'):
                print("________________________________________________________________")
                print(f"{GREEN}{item}{RESET} {BRIGHT_MAGENTA}<script file python>{RESET}")
                print("________________________________________________________________")
            elif item.endswith('.bat'):
                print("________________________________________________________________")
                print(f"{GREEN}{item}{RESET} {BRIGHT_MAGENTA}<script file batch>{RESET}")
                print("________________________________________________________________")
            elif item.endswith('.cmd'):
                print("________________________________________________________________")
                print(f"{GREEN}{item}{RESET} {BRIGHT_MAGENTA}<script file batch>{RESET}")
                print("________________________________________________________________")
            elif item.endswith('.zip'):
                print("________________________________________________________________")
                print(f"{GREEN}{item}{RESET} {BRIGHT_MAGENTA}<compressed file zip>{RESET}")
                print("________________________________________________________________")
            elif item.endswith('.sh'):
                print("________________________________________________________________")
                print(f"{GREEN}{item}{RESET} {BRIGHT_MAGENTA}<script file bash>{RESET}")
                print("________________________________________________________________")
            else:
                print("________________________________________________________________")
                print(f"{GREEN}{item}{RESET} {BRIGHT_MAGENTA}<file>{RESET}")
                print("________________________________________________________________")

def fakinstall(command):
    pkg = command[12:].strip()
    downurlpath = "https://fabischautest.github.io/FMOSfaks/"
    pkgfile = pkg + ".zip"
    downurl = downurlpath + pkgfile
    downpath = r"C:\FMOS\Programms\fak"
    fmospath = downpath[8:].strip()
    finalpath = os.path.join(downpath, pkgfile)
    
    print(f"{GREEN}Installing{RESET} {CYAN}{pkg}{RESET} {GREEN}from{RESET} {MAGENTA}{downurl}{RESET} {GREEN}to{RESET} {CYAN}{fmospath}{RESET}")

    response = requests.get(downurl)
    if response.status_code == 200:
        with open(finalpath, 'wb') as file:
            file.write(response.content)
        print(f"{GREEN}Downloaded successfully!{RESET}")

        pkg_folder = os.path.join(downpath, pkg)
        os.makedirs(pkg_folder, exist_ok=True)

        with zipfile.ZipFile(finalpath, 'r') as zip_ref:
            zip_ref.extractall(pkg_folder)
        
        print(f"{GREEN}Installation completed successfully!{RESET}")
    else:
        print(f"{RED}Error:{RESET} {BRIGHT_RED}Failed to download {pkg} from {downurl}{RESET}")
    
def faklistall():
    try:
        faklist = "https://fabischautest.github.io/FMOSfaks/list.txt"
        response = requests.get(faklist)
        if response.status_code == 200:
            content = response.text
            print(content)
        else:
            print(f"{RED}Error:{RESET} {BRIGHT_RED}Failed to retrieve content. Status code: {response.status_code}{RESET}")
    except requests.RequestException as e:
        print(f"{RED}Error:{RESET} {BRIGHT_RED}{e}{RESET}")
    
def fakremove(command):
    fakname = command[11:].strip()
    fakpathmain = r"C:\FMOS\Programms\fak"
    fakpath = os.path.join(fakpathmain, fakname)
    
    if not os.path.isdir(fakpath):
        print(f"{RED}Error:{RESET} {BRIGHT_RED}The FAK {CYAN}{fakname}{RESET} {BRIGHT_RED}is not a directory or does not exist.{RESET}")
        return

    confirmation1 = input(f"{YELLOW}Are you sure you want to delete the fak {RESET}{CYAN}'{fakname}'{RESET}{YELLOW} and all its contents? Type 'yes' to confirm: {RESET}").strip().lower()
    if confirmation1 != 'yes':
        print(f"{RED}Operation cancelled.")
        return

    confirmation2 = input(f"{YELLOW}Are you absolutely sure you want to delete the fak {CYAN}'{fakname}'{RESET}{YELLOW} and all its contents? Type 'yes' to confirm: {RESET}").strip().lower()
    if confirmation2 != 'yes':
        print(f"{RED}Operation cancelled.")
        return

    try:
        shutil.rmtree(fakpath)
        print(f"{GREEN}The fak {RESET}{CYAN}'{fakname}'{RESET} {GREEN}and all its contents have been deleted.{RESET}")
    except PermissionError:
        print(f"{RED}Error:{RESET} {BRIGHT_RED}Permission denied to delete the fak '{fakname}'.{RESET}")
    except FileNotFoundError:
        print(f"{RED}Error:{RESET} {BRIGHT_RED}The fak '{fakname}' was not found.{RESET}")
    except Exception as e:
        print(f"{RED}Error:{RESET} {BRIGHT_RED}{e}{RESET}")
    
def faklist():
    try:
        path = r"C:\FMOS\Programms\fak"
        entries = os.listdir(path)
        packages = [entry for entry in entries if os.path.isdir(os.path.join(path, entry))]
        print("FAK INSTALLED PACKAGES:")
        print()
        print("path: Programms\\fak")
        print()
        print("__________________________________________________")
        for package in packages:
            print(f"{package} <fak>")
            print("__________________________________________________")
    except FileNotFoundError:
        print(f"{RED}Error: {BRIGHT_RED}The path {path} does not exist.{RESET}")
    except PermissionError:
        print(f"{RED}Error:{RESET} {BRIGHT_RED}Permission denied to access the path {path}.{RESET}")
    except Exception as e:
        print(f"{RED}Error:{RESET} {BRIGHT_RED}{e}{RESET}")
    
def fakrun(command):
    fakname = command[8:].strip()
    fakpathmain = r"C:\FMOS\Programms\fak"
    fakmainfile = "main.py"
    fakpath = os.path.join(fakpathmain, fakname, fakmainfile)
    os.system('cls')
    process = subprocess.Popen(['python', fakpath])
    process.wait()
    os.system('cls')
    print(f"{GREEN}{fakname} has finished executing.{RESET}")
    
def help(command):
    helps = command[5:].strip()
    if helps == "commands":
        os.system('cls')
        print(commandlist)
        pause = input("Press enter to continue...")
        os.system('cls')
    elif helps == "system":
        os.system('cls')
        print(systemlist)
        pause = input("Press enter to continue...")
        os.system('cls')
    elif helps == "root":
        os.system('cls')
        print(helproot)
        pause = input("Press enter to continue...")
        os.system('cls')
    elif helps == "devmode":
        os.system('cls')
        print(helpdev)
        pause = input("Press enter to continue...")
        os.system('cls')
    else:
        print(f"{RED}ERROR:{RESET} {BRIGHT_RED}sorry i cant help you with that.{RESET}")
        print(f"{GREEN}Use 1 of these commands:{RESET}")
        print(helphelp)

def check_wifi_status():
    is_connected = False
    try:
        with socket.create_connection(("8.8.8.8", 53), timeout=2) as sock:
            is_connected = True
    except OSError:
        is_connected = False
    file_path = r"C:\FMOS\System\security\root\rootuser"
    file_exists = os.path.exists(file_path)
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{CYAN}WiFi Connected: {is_connected}{RESET}")
    print(f"{RED}Root Permissions: {file_exists}{RESET}")
    print(f"{GREEN}Current Date and Time: {current_datetime}{RESET}")

def runpy(command):
    pyname = command[7:].strip()
    if pyname.startswith('*'):
        pynamefinal = os.path.join(os.getcwd(), pyname[1:])
    else:
        pynamefinal = os.path.abspath(os.path.join(BASE_DIR, pyname))
    
    if is_devmode():
    
        if not pynamefinal.endswith('.py'):
            print(f"{BRIGHT_RED}ERROR: The file must be a Python script with a .py extension{RESET}")
            return
        sensitive_dirs = ['System', 'System\\security', 'System\\temp', 'System\\trash', 'System\\sys', 'System\\boot', 'Programms\\sys', 'Programms\\fak']
        if any(pynamefinal.startswith(os.path.join(BASE_DIR, sensitive_dir)) for sensitive_dir in sensitive_dirs):
            if not is_rooted():
                print(f"{BRIGHT_RED}ERROR: You are not rooted and cannot save to this directory!{RESET}")
                return
    
        current_dir = os.getcwd()
        pypath = pynamefinal
        os.system('cls')
        process = subprocess.Popen(['python', pypath])
        process.wait()
        os.system('cls')
        print(f"{GREEN}{pypath} has finished executing.{RESET}")
    else:
        print(f"{BRIGHT_RED}ERROR: You need to have developer mode enabled to run Python scripts (more info at help devmode){RESET}")

if os.name == 'nt':
    os.system('')
bootlogo()
fmosmainmenu()
