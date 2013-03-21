#Yeah, bitchez - time has come!
#Script gathering votes distribution on all questions on Stack Overflow
#version: 1.0 dirty
#author: QuteBits

#needs: python-2.7 and pyquery (if u dont the latter, run 'easy_install pyquery')
#works: automatically, leaving 'results_formatted.txt' in the end
#       though run it somewhere in a separate folder, because:
#takes: appr. 30 hours, 14GB memory for results (read: it also means 14GB traffic) pro 5m questions

#---------------------IMPORTS-----------------------
import sys

from urllib import urlopen        #for data download
from pyquery import PyQuery as pq #for parsing
from lxml import etree            #for parsing

#-------------------PREPARATIONS--------------------
url    = "http://stackoverflow.com/questions?page=1&sort=votes&pagesize=50" #we take first page
raw    = urlopen(url).read()                                                #with the most voted questions 
dom    = pq(raw)                                                            #generate DOM from its html
limit  = int(dom('.pager a').eq(4).attr('title').split(" ")[-1])            #extract number of pages to parse

limit_positive  = int(dom('.votes strong').eq(0).text())                    #extract the highest vote number

url    = "http://stackoverflow.com/questions?page=" + str(limit) + "&sort=votes&pagesize=50" #open the last page
raw    = urlopen(url).read()                                                #read its html
dom    = pq(raw)                                                            #generate DOM from it
limit_negative  = -int(dom('.votes strong').text().split(" ")[-1])          #extract the lamest vote number

#throw status message
sys.stdout.write("Overall " + str(limit) + " pages with votes ranging from " + str(-limit_negative) + " to " + str(limit_positive) + "\n")

domain = range(1,limit+1)

#------------------DATA DOWNLOADS-------------------
#---Here we download all html data from all pages---
sys.stdout.write("Downloading " + str(limit) + " pages:\n")

for i in domain:
	url = "http://stackoverflow.com/questions?page="+str(i)+"&sort=votes&pagesize=50"   #construct url
	#throw status message
	sys.stdout.write("Downloading page "+'{0:06}'.format(i)+" out of "+str(limit)+"\n")
	raw = urlopen(url).read()                         #download url
	f = open('result'+'{0:06}'.format(i)+'.txt', 'w') #create file
	f.write(raw)                                      #write to file
	f.close()                                         #close file

#------------------DATA PARSING---------------------
#-------Here we parse all the downloaded data-------
votes = ""

for i in domain:
	#throw status message
	sys.stdout.write("Parsing file "+'{0:06}'.format(i)+" out of "+str(limit)+"\n")     #construct url
	f = open('result'+'{0:06}'.format(i)+'.txt', 'r') #open file
	data = f.read()                                   #read from file
	d = pq(data)                                      #generate DOM from file data
	votes += d('.votes strong').text() + " "          #clip votes values and add 'votes'
	f.close()                                         #close file

#------------------DATA-FORMATTING------------------				
#----Here we format collected data before saving----
a = [0] * (limit_positive+1)                          #create array for positive voted questions
b = [0] * (limit_negative+1)                          #create array for negative voted questions

listing = votes.split(" ")                            #collect nr of questions for each vote number
for v in listing:
	if v != '':                                       #exclude last element of listing which is ''
		value = int(v)                                ##and remember...
		if value >= 0:                                ##it all will happen after 30 hours and
			a[value]+=1                               ##14GB traffic you've had with stackoverflow
		if value < 0:                                 ##dirty style
		    b[-value]+=1

formatted = ""	   #final string that we will save in the end
sum=0              #kind of a checksum

for i in range(1,limit_negative+1):
	if b[13-i] > 0:
		formatted += str(i-13) + " votes: " + str(b[13-i]) + "\n"
		sum+=b[13-i]

for i in range(0,limit_positive+1):
	if a[i] > 0:
		formatted += str(i) + " votes: " + str(a[i]) + "\n"
		sum+=a[i]
		
formatted += "SUM OF ALL QUESTIONS: " + str(sum)      #kind of a summary line reminding you of the
                                                      #awesomeness you've made running that script

f = open('result_votes_formatted.txt', 'w')           #create final file
f.write(formatted)                                    #write the result down
f.close()                                             #THE END