#this is the first stage of the program
#Supported Commands
#   -delete_language delete <language>
#   -enter_language "dive <language>"
#   -create_project "create <language> <project_name> "--This is to be handled here because we will assign under what programming category our project is to be written under
#   -help "-help", outputs the comments above.

from S_stage import ProjectHandler
import os
import string
import shutil

class LanguageHandler():
    varHelper = "delete <language> -- deletes the entire folder \n" + "dive <language> -- enter the specified language \n" + "create <language> <project_name> -- Create a project under a specific language \n" + "atom\n" + "show <language>\n" + "show\n" + "clear\n" + "quit"
    path = "/home/sc/Documents/code/"
    inProject = False
    projectHandler = ProjectHandler() #Project_Handler

    def __init__(self):
        #Instead of hardcoding 'sc' make the program flexible so that it picks the correct usr

        #if the path to code doesn't exist
        if(not os.path.exists(self.path)):
            os.makedirs(self.path)
        #Set the working directory
        os.chdir(self.path)

    #Print all of the languages again
    def __printAll__(self):
        outputVal = ''
        for folders in os.listdir(self.path):
            subCount = 0
            for sub in os.listdir(folders):
                subCount += 1
            outputVal += folders + '[' + str(subCount) + '] | '

        print(outputVal)

    #here we handle update data
    def update(self, input):
        #if we have input more than 1 argument
        input = input.lower()
        l_input = input.split(' ')

        if(self.inProject):
            self.projectHandler.update(input)
            if(input == "jump"):
                self.inProject = False
                os.chdir(self.path)
            return()


        if(len(l_input) > 1):
            self.__multiple_input__(l_input)
        else:
            #This should encompase all of the single word calls
            if(l_input[0] == "-help"):
                print(self.varHelper)
            elif(l_input[0] == "show"):
                self.__printAll__()
            elif(l_input[0] == "atom"):
                os.system("atom .")
            else:
                print("Type -help for help")

    def __multiple_input__(self, l_input):
            #Create
            if(l_input[0] == "create"):
                if(len(l_input) > 3):
                    print("invalid input")
                    return()
                #if the language doesn't exist, create it and the project path
                if(not os.path.exists(l_input[1])):
                    os.makedirs(l_input[1])
                    if(len(l_input) > 2):
                        os.makedirs(l_input[1] + "/" + l_input[2])
                    return()
                #If the project path doesn't exist then create one
                if(not os.path.exists(self.path + l_input[1] + "/" + l_input[2])):
                    os.makedirs(self.path + l_input[1] + "/" + l_input[2])
                else:
                    print("Project title already exists")
            #Delete
            elif(l_input[0] == "delete"):
                if(os.path.exists(self.path + l_input[1])):
                    shutil.rmtree(l_input[1])
                    return()
                print("invalid input")

            #Enter
            elif(l_input[0] == "dive"):
                if(os.path.exists(self.path + l_input[1])):
                    self.projectHandler.openProject(self.path + l_input[1])
                    self.inProject = True
            elif(l_input[0] == "show"):
                if(os.path.exists(self.path + l_input[1])):
                    self.__printFolder__(l_input[1])

    def __printFolder__(self, folderName):
        output = ""
        for folder in os.listdir(self.path + folderName):
            output += folder
        print(output)
