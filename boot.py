import os
import time
import keyboard

def check_files_and_log_errors():
    file_paths = [
        r'C:\FMOS\System\sys\main.cmd',
        r'C:\FMOS\System\sys\main.py',
        r'C:\FMOS\System\boot\boot.bat',
        r'C:\FMOS\System\boot\boot.py',
        r'C:\FMOS\System\sys\usr'
    ]
    log_file_path = r'C:\FMOS\System\boot\boot.log'
    missing_files = [path for path in file_paths if not os.path.isfile(path)]
    if missing_files:
        error_message = 'Missing Sys Files:\n' + '\n'.join(missing_files) + '\n'
        print(error_message)
        with open(log_file_path, 'a') as log_file:
            log_file.write(error_message)
        with open(log_file_path, 'r') as log_file:
            log_content = log_file.read()
            print('Content of log file:\n', log_content)
    else:
        exit()

def press_f11():
    keyboard.press_and_release('f11')
press_f11()
os.system('')
file_path = r'C:\FMOS\System\boot\boot.log'
with open(file_path, 'w') as file:
    file.write('Boot:\n')
check_files_and_log_errors()