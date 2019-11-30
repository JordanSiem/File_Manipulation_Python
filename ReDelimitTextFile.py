import glob
import pandas as pd
print("This program is used to re-delimit files. Also as a note, it will also combine all text files within the folder "
      "you specify so try to run this in a separate folder if need be.")
print("In order to combine files, the files should have the same number of columns and headers. "
      "Do not worry about deleting the headers in each file.")
print("")
pathname = input('Where are the files located? (Please give me the file path):')
print("")
print("Please choose one of the following options with a number...")
print("")
print("Delimit text files by:")
print('     1) Pipe ("|")')
print('     2) Comma (",")')
print('     3) Semi-Colon (";")')
print("")
option_type = input('Which option would you like?')
str(option_type)

#Text files to pipe delimited...also this will combine all the text files into the folder to one file pipe delimited.

if option_type == '1':
    option_type = 'txt'
    files = glob.glob(r'{pathname}/*.{option_type}'.format(pathname=pathname, option_type=option_type))
    combined_file = pd.concat([pd.read_csv(f, index_col=0, sep='\t') for f in files])
    combined_file.to_csv(pathname + "\\" + 'Combined.txt', sep='|')  # change to pathname

#This will just combine all the csv files together that are in a folder into a comma seperated text file.

elif option_type == '2':
    option_type = 'csv'
    files = glob.glob(r'{pathname}/*.{option_type}'.format(pathname=pathname, option_type=option_type))
    combined_file = pd.concat([pd.read_csv(f, index_col=0) for f in files])
    combined_file.to_csv(pathname + "\\" + 'Combined.txt', sep=',')  # change to pathname

#This will combine all xlsx files together to a text file seperated by semi-colon.

elif option_type == '3':
    option_type = 'xlsx'
    files = glob.glob(r'{pathname}/*.{option_type}'.format(pathname=pathname, option_type=option_type))
    combined_file = pd.concat([pd.read_excel(f, index_col=0) for f in files])
    print(combined_file)
    combined_file.to_csv(pathname + "\\" + 'Combined.txt', sep=';')  # change to pathname

else:
    input("Invalid response. Hit Enter to exit.")
