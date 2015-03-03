## CSV Data Munger/Cleaner/Shaper
# Created by: Mitch Main
# Created on: 9/25/14
# Info: This imports a CSV file to be cleaned, allows you to define the number
#       of fields you would like to import, and then imports them from the file,
#       then it writes it to a cleaned file

# Imports
import csv
import tkinter
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import string
import itertools
import re



## FUNCTION: GetFile()
# The GetFile function gives the user a GUI interface to get the file directory
# the function then returns a file directory as a string.
# @input: From UI Dialog Box
# @return str: filedir
# @return int: collumn

def GetFile():
    filedir = askopenfilename(title='Open File')
    return filedir



##FUNCTION: TxtWriter(fieldList, headerList)
# TxtWriter writes the the field lists to the output file as a tab delimited file
# for easy uploading to a SQL server or to be easily opend by Excel
# @input List : fieldList
# @input List : headerList
# @return file: .txt file in saveas location

def TxtWriter(fieldList, headerList):

    #important variables
    writeList = []

    #get filename for writefile and open it
    filename = asksaveasfilename(title='Save As :', defaultextension='.txt')
    with open(filename, mode='w', newline = '') as wfile:
        writer = csv.writer(wfile, dialect='excel-tab')

        #write the headers
        if headerList:
            writer.writerow(headerList)

        #iterate over the 'rows'
        for row in range(len(fieldList[0])):
            #iterate over the 'collumns'
            for col in range(len(fieldList)):
                writeList.append(fieldList[col][row])
            #end for-loop
            writer.writerow(writeList)
            writeList.clear()
        #end for-loop
    #end with-block



#FUNCTION: GetUserInput(prompt, errorMessage)
# This is a helper function to get input and avoid repeating code
# @input str: prompt
# @input str: errorMessage
# @return str: inputString

def GetUserInput(prompt, errorMessage, typeCheck):
    while True: #Can I say that, this while loop is not my code, and I hate its style. However, it works!
        if typeCheck == 'int':
            try:
                _input = int(input(prompt))
            except ValueError:
                print(errorMessage)
                continue
            else:
                print("Valid input")
                break
        elif typeCheck == 'bool':
            try:
                _input = bool(input(prompt))
            except ValueError:
                print(errorMessage)
                continue
            else:
                print("Valid input")
                break
        #end if-elif block
    #end while-loop

    return _input

#FUNCTION: FieldImporter(filedir)
# This functions grabs the fields by each line and stores them in the dynamic list
# @input str : filedir
# @return list: fieldList
# @return list: headerList

def FieldImporter(filedir):

    #instantiations
    fieldLocations = []
    headerList = []

    #Get the number of fields to import
    howManyFields = GetUserInput('How many fields to import? ', 'Not an int', 'int')

    #Instantiate the main list
    fieldList = [[] for i in range(howManyFields)]

    #get field locations (will account for human counting later)
    print('Input the collumn numbers in the order you want them to appear in the output file')
    print('i.e. If you want the 5th collumn in the 1st collumn of the output list,')
    print('give me 5 as the first entry then list the rest as you like')
    for i in range(howManyFields):
        fieldLocations.append(GetUserInput('Collumn number of field to be imported', 'Thats not an integer', 'int'))
    #end for-loop
    
    #Get Headers
    hasHeaders = GetUserInput('Does your data have headers? (Use: True/False or 1/0)', 'Not a boolean value', 'bool')
    if hasHeaders:
        importHeaders = GetUserInput('Want to import your headers? (Use: True/False or 1/0)', 'Not a boolean value', 'bool')
    #end if-block

    if not importHeaders:
        makeHeaders = GetUserInput('Want to create headers for your data?\nNote: Only make headers for the fields you will import')
    else:
        makeHeaders = False
    #end if-else

    if makeHeaders:
        for i in range(howManyFields):
            headerList.append(GetUserInput('Header name for field: ', 'Not an integer', 'int'))
    firstLine = GetUserInput('Which row is the first line of data (give line with the headers on it)', 'Not an interger', 'int')

    #open the file and start reading
    with open(filedir) as csvfile:
        reader = csv.reader(csvfile, dialect='excel')
        if importHeaders:
            headerLoop = True
        else:
            headerLoop = False
        for i in range(firstLine - 1): #skip the lines til the first line
            next(reader)
        for row in reader:
            if headerLoop:
                for i in range(howManyFields):
                    headerList.append(row[fieldLocations[i] - 1])
                #end for-loop
                headerLoop = False
            else:
                for i in range(howManyFields):
                    #use the fieldLocations and iterate through their locations and get them from the row iterable
                    fieldList[i].append(row[fieldLocations[i] - 1]) #account for human counting
                #end for-loop
            #end if-else block
        #end for-loop
    #end with-block
    return fieldList, headerList

    

# MAIN ALGORITHM

def main():

    filedir = GetFile()
    fieldList, headerList = FieldImporter(filedir)
    TxtWriter(fieldList, headerList)


#RUN IT!!

main()
    
