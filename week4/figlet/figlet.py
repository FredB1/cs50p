from sys import argv,exit
from pyfiglet import Figlet
from random import choice
figlet = Figlet()
fonts = figlet.getFonts()

if len(argv) == 1 or len(argv)==3:
    
    if len(argv)==1:
        str = input("Input: ")
        figlet.setFont(font=choice(fonts))
    if len(argv)==3 and (argv[1]=="-f" or argv[1]=="--font"):
        if argv[2] in fonts:
            figlet.setFont(font=argv[2])
            str = input("Input: ")
        else:
            exit("Invalid usage1")
    else:
            exit("Invalid usage2")
    
    print(figlet.renderText(str))
else:
            exit("Invalid usage3")