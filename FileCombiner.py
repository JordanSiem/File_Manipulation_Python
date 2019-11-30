import glob
import pandas as pd
print("This program is used to combine files. Your options will be txt to txt, csv to txt, xlsx to txt, csv to csv,"
      " and xlsx to xlsx")
print("In order to combine files, the files should have the same number of columns and headers. "
      "Do not worry about deleting the headers in each file.")
print("")
pathname = input('Where are the files located? (Please give me the file path):')
print("")
print("Please choose one of the following options with a number...")
print("")
print("To Text File:")
print("     1) TXT file to TXT file (.txt)")
print("     2) CSV file to TXT file (.txt)")
print("     3) XLSX file to TXT file (.txt)")
print("Other:")
print("     4) CSV file to CSV file (.csv)")
print("     5) XLSX file to XLSX file (.xlsx)")
print("")

#Thought number would be easiest way to stop answer variations.

option_type = input('Which option would you like?')
str(option_type)

if option_type == '1':
    option_type = 'txt'
    #for files that end txt combine them.
    files = glob.glob(r'{pathname}/*.{option_type}'.format(pathname=pathname, option_type=option_type))
    combined_file = pd.concat([pd.read_csv(f, index_col=0, sep='\t') for f in files])
    combined_file.to_csv(pathname + "\\" + 'Combined.txt', sep='\t')  # change to pathname
elif option_type == '2':
    option_type = 'csv'
    #for files that end in csv come them and make into text file.
    files = glob.glob(r'{pathname}/*.{option_type}'.format(pathname=pathname, option_type=option_type))
    combined_file = pd.concat([pd.read_csv(f, index_col=0) for f in files])
    combined_file.to_csv(pathname + "\\" + 'Combined.txt', sep='\t')  # change to pathname
elif option_type == '3':
    option_type = 'xlsx'
    #for files that end in xlsx come them and make into text file.
    files = glob.glob(r'{pathname}/*.{option_type}'.format(pathname=pathname, option_type=option_type))
    combined_file = pd.concat([pd.read_excel(f, index_col=0) for f in files])
    print(combined_file)
    combined_file.to_csv(pathname + "\\" + 'Combined.txt', sep='\t')  # change to pathname
elif option_type == '4':
    option_type = 'csv'
    #for files that end in  csv just combine them as a csv
    files = glob.glob(r'{pathname}/*.{option_type}'.format(pathname=pathname, option_type=option_type))
    combined_file = pd.concat([pd.read_csv(f, index_col=0,error_bad_lines=False) for f in files])
    combined_file.to_csv(pathname + "\\" + 'Combined.csv')  # change to pathname
elif option_type == '5':
    option_type = 'xlsx'
    #for files that end in xlsx just combine them as a xlsx
    files = glob.glob(r'{pathname}/*.{option_type}'.format(pathname=pathname, option_type=option_type))
    combined_file = pd.concat([pd.read_excel(f, index_col=0) for f in files])
    combined_file = combined_file.to_excel(pathname + "\\" + 'Combined.xlsx', index=None, header=True)
else:
    input("Invalid response. Hit Enter to exit.")
