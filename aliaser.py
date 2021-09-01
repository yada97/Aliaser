#! /usr/bin/python3

#Built for Orion Group Simple scripts for daily use
"""
If you are using bash change the following lines to [.bashrc] 47, 51, 64 ,65
Built for Orion group pair programmers
If you have a large cluster of folders uncomment Threading 2

"""

import time
import sys
import pathlib
import os
import argparse
from colorama import Fore
from pathlib import Path
from threading import Thread

home = str(Path.home()) + "/"

stress_location = os.getcwd()

def art():
    print(f"""{Fore.RED}
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%             /@@
    @@@@@@/    @@@@@@@@   %@@@@@@@@@(  @@@@@@@@    #@@@@&   .@@@@@@#  #@@
    @@@@@@     *@@@@@@@   @@@@@@@@@@/  @@@@@@@*     @@@@&  ,@@%    .  (@@
    @@@@@/      &@@@@@@   @@@@@@@@@@. *@@@@@@@      ,@@@&   @@/       /@@
    @@@@@   #.   @@@@@@   @@@@@@@@@@   @@@@@@,   &   /@@%   (@@@%.    @@@{Fore.GREEN}
    @@@@*  *@@   (@@@@@  .@@@@@@@@@@,  @@@@@@   @@(   @@@        /@/  &@@
    @@@@          @@@@@  .@@@@@@@@@@.  @@@@@,         (@%         (#  /@@
    @@@   (@@@@(   @@@@   @@@@@@@@@@.  @@@@#   @@@@&   &%   @@/   &@  /@@
    @@(   @@@@@@   *@@@   ((/(&@@@@@,  @@@@   @@@@@@(   %    &@@@@@#  #@@
    @@@@@@@@@@@@@@@@@@@,        @@@@@@@@@@@@@@@@@@@@@@@@%             (@@
                {Fore.WHITE}copyright Orion {Fore.GREEN}2021
    """)

def alias_workout(w_path, process, delay, repeat):
    for path in pathlib.Path(w_path).iterdir():
        if path.is_dir():
            os.chdir(w_path)
            chosen_path = path.stem
            #src = stress_location + "/"+ chosen_path
            alias = "alias " +chosen_path+"="+ "\"" +w_path+"/"+chosen_path+ "\""

            #Main program writes to .zshrc and stores your aliase ther
            f = open(home + ".zshrc", "a")
            f.write(alias + "\n")
            f.close()
            os.system("zsh")
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
def reset_alias():
    os.system("grep -Fvxf $HOME/.alias_catalog $HOME/.zshrc >> temprc ")
    os.system("mv temprc $HOME/.zshrc")
    os.system("rm -rf $HOME/.alias_catalog &>/dev/null")
    os.system("rm -rf $HOME/aliasnames &> /dev/null")
    print(f"{Fore.RED}RESET COMPLETE")

def Main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Enter the path e.g [-p /path/todidr] [--path /path/todir]")
    parser.add_argument("-a", "--auto", help="E.g [-a auto] or [--auto auto] for current directory")
    parser.add_argument("-r", help="Resets already set variables to default settings")
    args = parser.parse_args()

    if args.path:
        w_path = args.path
        t1 = Thread(target=alias_workout, args=(w_path, "process_1", 1,2))
        #t2 = Thread(target=alias_workout, args=(w_path, "process_2", 1,3))
        t1.start()
        #t2.start()
    elif args.auto:
        if args.auto == "auto":
            w_path = os.getcwd()
            t1 = Thread(target=alias_workout, args=(w_path, "process_1", 1,2))
            #t2 = Thread(target=alias_workout, args=(w_path, "process_2", 1,3))
            t1.start()
            #t2.start()
        else:
            print(f"{Fore.RED} Usage ./aliaser.py -a auto, For current directory")
    elif args.r :
        if args.r == "reset":
            reset_alias()
            os.system("zsh")
        else:
            print(f"{Fore.RED} Usage ./aliaser.py -r reset, To reset config to Default")
    else:
        os.system("clear")
        art()
        len(sys.argv)==1
        parser.print_help(sys.stderr)
        sys.exit(1)

if __name__== "__main__":
    Main()















































