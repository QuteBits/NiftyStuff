#Yeah, bitchez - time has come!
#Script renaming files in the current directory according to 'rename.txt'
#version: 1.0 dirty
#author: QuteBits

#'rename.txt' should be written in the following format:
#current_filename_1.mp3 new_filename_1
#current_filename_2.mp3 new_filename_2
#...                    ...

import os
import string

valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits) #valid filename chars

f = open("rename.txt", "r")       #open your 'rename.txt'

for line in f.read().split('\n'): #read a line and:
  print line                      #throw status message
  y = line.find(" ")
  name_old = line[:y]
  name_new = line[y+1:].strip() + ".mp3"
  name_new = ''.join(c for c in name_new if c in valid_chars)
  print name_old                  #throw status message
  print name_new                  #throw status message
  print os.path.isfile(name_old)  #throw status message
  if os.path.isfile(name_old):
    os.rename(name_old, name_new) #rename file

f.close()                         #THE END