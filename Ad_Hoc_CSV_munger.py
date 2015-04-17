## Ad-Hoc Analysis: CSV Data Munger/Cleaner/Shaper
# Created by: Mitch Main
# Created on: 9/25/14
# Info: This is a specified munger which consumes a csv from an Ad-Hoc Analysis
#       report and then columnizes the data. This particular version, columnizes
#       a report which has visits to a site section brokendown by user_id (evar03).
#       This create columns for user_id, month_of_visit

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


#FUNCTION: ParseFields(filedir)
# This does all the heavy lifting and builds the two columns
# return: fields_to_write

def ParseFields(filedir):
    user_id = []
    date = []
    visits = []
    
    with open(filedir, newline = '') as csvfile:
        reader = csv.reader(csvfile, dialect = 'excel')
        headers = next(reader)
        for row in reader:
            for i in range(1, len(row)):
                if(int(row[i]) > 0):
                    user_id.append(row[0])
                    date.append(headers[i])
                    visits.append(row[i])
                #end if-block
            #end for-loop
        #end for-loop
    #end with-block

    filename = filedir[ :-4] + '_cleaned.csv'

    with open(filename, mode = 'w', newline = '') as writefile:
        writer = csv.writer(writefile, dialect='excel')
        writer.writerow(['user_id', 'date', 'visits'])
        for i in range(0,len(user_id)):
            writer.writerow([user_id[i], date[i], visits[i]])
        #end for-loop
    #end with-block

#end def


def main():
    ParseFields(GetFile())
#end def

main()
                    


