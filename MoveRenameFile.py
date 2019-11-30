import os
import datetime

#List what is in drive
x = os.listdir('J:\Hold')


y = 'J:\Hold\\'


#Change working drive
os.chdir('J:\Hold')


#For loop to change file name to have the name and modification time in same name.

for file in x:
    print(file)

    #Path to file and file name
    file2 = y + file

    #Modification time
    modTimesinceEpoc = os.path.getmtime(file2)
    modificationTime = datetime.datetime.fromtimestamp(modTimesinceEpoc)

    modificationTime = str(modificationTime)
    modificationTime = modificationTime.replace("-", "")
    modificationTime = modificationTime.replace(":", "")
    modificationTime = modificationTime.replace(" ","")

    #Take off the extension
    newfile = file.replace(".txt", "")

    #Adding the modification time to the name of file and putting extension back on.
    os.rename(file, newfile + modificationTime + '.txt')



