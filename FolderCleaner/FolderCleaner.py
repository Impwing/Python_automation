#I was bored so I created a downloads cleaning program
#When this program runs then it moves the different files
#that you might have in your ~/Downloads/ file, and places
#them into a folder that is known as ~/Files/
import os

def _FolderCleaner_():
    #Change the working directory
    os.chdir("/home/sc/")
    #Setup variables
    downloads = "Downloads/"
    dir = os.listdir(downloads)

    #if Files/ doens't exist then create it
    if(not os.path.exists("Files/")):
        os.mkdir("Files/");

    #loop through all the files
    for file in dir:
        #Get the extension of the file
        file_extension = os.path.splitext(file)[1]

        #Split the extension and just get the final characters
        destination = file_extension.split(".")
        destination = "Files/" + file_extension.split(".")[1] + "/"

        #If the path for the file does not exist
        if(not os.path.exists(destination)):        
            #Create a folder for those specific files
            os.mkdir(destination);

        #Move all of the files that end in .deb
        os.rename("Downloads/" + file, destination + "/" + file)



_FolderCleaner_()
