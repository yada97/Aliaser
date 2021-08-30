#! /usr/bin/python3

#Built for Orion Group Simple scripts for daily use


import pathlib
import os
from colorama import Fore
from pathlib import Path


clear = lambda:system('clear')
home = str(Path.home()) + "/"

stress_location = os.getcwd()
print("""
        CURRENTLY BEING BUILT

        Run this script From the folder which you wish to alias

        """)

def program():
    for path in pathlib.Path(stress_location).iterdir():
        if path.is_dir():
            chosen_path = path.stem
            src = stress_location +"/"+ chosen_path
            alias = "alias " +chosen_path+"="+ "\"" +stress_location+"/"+chosen_path+ "\""
            
            #Main program writes to .zshrc and stores your aliases
            f = open(home + ".zshrc", "a")
            f.write(alias + "\n")
            f.close()
            
            #Temporary files will be used when the need to delete a folder arises
            f = open(home + ".alias_catalog", "a")
            f.write(alias +"\n")
            f.close()

            #Remembrance file so you can remember the names you aliased
            f= open(home + "aliasnames", "a")
            f.write(chosen_path +"\n")
            f.close()
            print(f"{Fore.YELLOW}You can now use this as a shortcut")
            print(f"{Fore.RED}"+chosen_path)

program()
