# Input Options.
#   -delete_project --Remove a project folder with all of its contents
#   -rename_project --Rename a specific project
#   -jump           --Jumps up into the language view

import os
import shutil

class ProjectHandler():
    projectPath = ""

    #This should be assigned
    def openProject(self, path):
        #Change directory
        os.chdir(path)
        self.projectPath = path

    def update(self, input):
        l_input = input.split(' ')
        #show all projects within the language
        if(input == "show"):
            output = ""
            for folders in os.listdir(self.projectPath):
                output += folders + " | "
            print(output)
        #delete
        if(l_input[0] == "delete"):
            if(os.path.exists(l_input[1])):
                shutil.rmtree(l_input[1])
                print("removed " + l_input[1])
