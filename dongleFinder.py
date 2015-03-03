#=====================================================================================#
# CSV Data Munger/Cleaner/Shaper
# Created by: Mitch Main
# Created on: 9/25/14
# Info: Custom build reporter takes a CSV and then prepares a couple of fields by
#       parsing the subject line required in an analysis.
#=====================================================================================#

#imports required
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


##FUNCTION: csvWriter(fieldList, headerList)
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

#FUNCTION: 
