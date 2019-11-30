import os
import zipfile

print("This executable is used to extract documents from zip folders. A new folder will be created with the zip folder "
      "name + 1. This program will process through the folder structure and unzip all zip folders in subdirectories.")
print("")
print("Instructions:")
print("-First, tell the program where you'd like to start the process.")
print('-And as always, please hit "enter" when prompted in order to close and end the program.')
print("")
print("")

start = input("Where to start?")

#Will start traversing through directories/sub directories depending upon where told to start


for (root, dirs, files) in os.walk(start):
    #root is file path in all directories/sub
    #dirs folders in file path or in directories/sub
    #files....listing of files in directories/sub
    #os.walk is the command for the traversing

    for x in files:
        #x = file name

        #rebuilding path to file
        here = root + '\\' + x

        #files that end in zip
        if here.endswith('.ZIP') or here.endswith('.zip'):

            #I kept getting an error for zip folders already extracted so added try statement to ignore if
            #it waa already done.
            try:
                zip = zipfile.ZipFile(here, 'r')
                #make folder
                os.mkdir(here + '1')
                zipfolder = here + '1'
                zip.extractall(path=zipfolder)
            except:
                print("Ignoring Error: " + x + " was already extracted")
        else:
            pass

input("Zip files extracted....Have a great day!")
