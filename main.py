################################
### CODE BY @mikey_developer ###
### Simple python terminal   ###
################################

import os
import time
import pyautogui as pgg
from colorama import init
from termcolor import colored
import webbrowser as wbb
import playsound as pss

init()

green = "green"

FILE_CREATED = "+ file: "
FILE_REMOVED = "- file: "
M_DIR = "+ dir: "
R_DIR = "- dir: "
R_FILE = "FILE: "
VERSION_IS = "24.01\nby @mikey_developer"
SAVED = "Saved! file: "
PLAYING = ">> "

print(colored("----------------------", "green"))
print(colored("|", "green"), colored("    Colibri", "cyan"), colored("       | :: ====== :: ", "green"))
print(colored("---------------------- ", "green"))
print()

DOCS = """
    cr => dir name - new directory
    dd => dir name - remove directory
    df => file name - remove file 
    rf => file name - read file 
    cf => file name - create file
    wf => file name - write file
    go => web site name - browser
    pl => audio - playing audio
    st => app name - opening app
    cocl => clear

       """

while 1:
    command_is = input(colored("l: ", "green"))
    if command_is.startswith("cr => "): #new directory (mkdir)
        os.mkdir(f"{command_is[6:]}")
        print(M_DIR + command_is[6:])

    elif command_is.startswith("dd => "): # remove directory 
        os.rmdir(f"{command_is[6:]}")
        print(R_DIR + command_is[6:])

    elif command_is.startswith("df =>  "): # removing files
        os.rm(f'{command_is[6:]}')  
        print(FILE_REMOVED + command_is[6:])

    elif command_is.startswith('rf => '):
        # print(R_FILE + command_is[6:])
        with open(command_is[6:], 'r+') as f:
            read = f.read()
        print(R_FILE + command_is[6:])
        print(read)

    elif command_is.startswith('cf => '):
        # print(R_FILE + command_is[6:])
        with open(command_is[6:], 'a') as f:
            f.write('#')
        print(FILE_CREATED + command_is[6:])

    elif command_is.startswith('wf => '):
        # print(R_FILE + command_is[6:])
        note = input("l:: ")
        with open(command_is[6:], 'w') as f:
            f.write(f'{note}')
        print(SAVED + command_is[6:])

    elif command_is.startswith('go => '):
        wbb.open("https://ya.ru/search/?text=" + command_is[6:])

    elif command_is.startswith('pl => '):
        print(PLAYING + command_is[6:])
        pss.playsound(command_is[6:] + '.mp3')

    elif command_is.startswith('st => '):
        print(PLAYING + command_is[6:])
        os.startfile(command_is[6:])


        

    elif command_is == "cl :: ver": # version
        print("version: " + VERSION_IS)

    elif command_is == "dcs": # docs
        print("docs:\n\n" + DOCS)

    elif command_is == "cocl": # clear
        os.system('cls')
        print(colored("----------------------", "green"))
        print(colored("|", "green"), colored("    Colibri", "cyan"), colored("       |", "green"))
        print(colored("---------------------- ", "green"))
        print()

    else:
        pgg.alert(title = "Terminal", text = "Error: Command")
