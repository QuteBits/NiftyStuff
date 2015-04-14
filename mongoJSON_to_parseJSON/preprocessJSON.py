#Yeah, bitchez - time has come!
#Script wrapping JSON (converted from MongoDB BSON dump) with some stuff for Parse.com
#version: 1.0 dirty
#author: QuteBits

#---------------------IMPORTS-----------------------
import sys

#----------------------WORK-------------------------
#BSON was taken from MongoDB dump here: https://github.com/kapilreddy/Shabda-Sangraha
#then it was converted to JSON using MongoDB tools and named words.json 
raw = open('words.json', 'r').read()
#eliminate all . and $ characters from the column (parse doesn't accept them)
result = '"olderId":{"oid":"'.join(raw.split('"_id":{"$oid":"'))

#join and wrap the stuff - it's better than doing it in a for loop because you will not have to
#delete the comma after the last element (it's important, with an unnecessary comma
#parse will not validate your JSON)
result = '},{'.join(result.split('}\n{'))
result = '{ "results": [ ' + result + ']}'

#save
f = open('result.json', 'w')
f.write(result)
f.close()
