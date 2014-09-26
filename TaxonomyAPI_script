##TaxonomyAPI_Script
# Author: Mitch Main
# Last Updated: 8/18/14
# Important Notes: This file does not handle headers (make sure you manually rid the headers)
#                  Please be sure to filter file for repeats, this can only handle 1000 calls
#                  so make the best of those API calls.
# Input: .csv file with one field having URLs to process
# Output: .csv file with URLs processed, Taxonomy outputted,
#          and Possible Error Messages


#import necessary modules and packages
import csv
import json
from alchemyapi import AlchemyAPI
import requests

#Necessary Variables
writerHeader = ['URL', 'Category', 'Score']
API_KEY = '0b3ee55129964c53258bab520d8211b1d6d2f5e3'
alchemyapi = AlchemyAPI()
limit = 990; #default 100
counter = 0 #counter to track the number of iterations
writeList = [] #list to keep write rows in.

#get filePath from user
path = "C:\\Users\\mitch.main\\Documents\\DataFolders\\URLsForScript.csv" 

#trap for correct filetype
##while readFile[-4:]!= '.csv':
##    print('Invalid file type -- must be .csv')
##    readFile = input("CSV File with URLs :") 
#end loop

#open file and create reader
with open(path, 'rt') as readFile:
    reader = csv.reader(readFile, dialect = 'excel')

    URL_List = [row for row in reader]

#close reader

#instantiate new .csv file with name "file_results.csv" and open the writer
w_file = path[:-4]+'_results.csv'
with open(w_file, 'wt') as csvFile:
    writer = csv.writer(csvFile, delimiter = ',')
    
    #Initialize the header in the file    
    writer.writerow(writerHeader)

    for url in URL_List: #iterating over the reader
        if counter < limit: #check that variable set to desired value above ^^
            response = alchemyapi.taxonomy('url',url)#call the API
            print('Call # ' + str(counter))
            if response['status'] == 'OK': #if no errors
                response = json.loads(json.dumps(response))
                taxonomy = response['taxonomy']
                for category in taxonomy: #write all three categories and scores
                    writeList.append(url)
                    writeList.append(category['label'])
                    writeList.append(category['score'])
                #end loop
            else: #if errors denote with NULL values in categories
                writeList = [url, 'NULL', '0.0']
            #end if-else
            writer.writerow(writeList)
            writeList.clear()
            counter+=1
        else:
            break
        #end if-else
    #end loop
#File closes automatically in 'with' statement and we can exit
print('Done')
#end of script
