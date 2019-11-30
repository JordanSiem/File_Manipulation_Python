import os

print("This executable is used if you are looking for specific files names, folder names, broker names etc.")
print("")
print("Instructions:")
print("-First, tell the program a subtext you are looking for (examples: Med.txt, Rx...etc.).")
print('-Next, tell it a starting point.')
print("Lastly, please close program when finished as I run FOREVER!!!!")
print("")
print("")

target = input("What are you looking for?")

#Forever loop....this allows for the program to find matches and if you have not found what you are looking for
#, you can check another place. If you need to change your search criteria then you will have to rerun program.

while 1 == 1:

    start = input("Where should I start looking?")
    #The program will keep asking you where to start looking by design cause I'm assuming if you don't find it the
    #first time, you can check somewhere else.

    for (root, dirs, files) in os.walk(start):
        #os.walk is used for traversing in for loop
        #root = file path
        #dirs = folders
        #files = files

        x = root
        filelist = os.listdir(x)

        for files in filelist:

            #rebuilding file path to exact file
            here = x + '\\' + files

            if target in here:
                print(here)
            else:
                pass
