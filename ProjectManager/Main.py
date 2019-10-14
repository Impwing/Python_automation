#What is this script supposed to do?
#The script is meant to be a sort of project folder manager.
#This should manage all of the code projects that you want to create on a linux machine.

# 'Check to see if the "Code" folder exists' -- if not the ask the user for a name and create it
# print all of the different language projects that exist i. e
#   CS -> js
#   CS -> py
#   CS -> C
#   CS -> C++
#   CS -> Ruby
# input: ...

# At this stage the user may want to input the following:
#   -delete_language DONE
#   -enter_language
#   -create_project DONE --This is to be handled here because we will assign under what programming category our project is to be written under

# Input Options.
#   -delete_project --Remove a project folder with all of its contents
#   -rename_project --Rename a specific project
#   -jump           --Jumps up into the language view
#   -open_project   --Should open a terminal in this directory. As well as atom.

#Static inputs:
# -quit | DONE |
# -help ----This is to vary based upon what stage the user is on | DONE |
# -about ----Prints information about the author

from F_stage import LanguageHandler
import os

def _main_():

    #input variable
    input = ""

    #clear the terminal
    os.system("clear")

    #initialization stage
    m_langHandler = LanguageHandler()


    while(True):
        input = raw_input("input: ")
        if(input == "quit"):
            break

        if(input == "clear"):
            os.system("clear")
        else:
            m_langHandler.update(input)



_main_()
