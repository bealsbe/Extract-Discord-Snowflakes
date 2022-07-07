from tkinter import Tk
import re
import os
import time

if not os.path.exists('output'):
    os.makedirs('output')

def getSnowflakes(rawtext):
     return re.findall('\d{17,19}', rawtext)

def writeResults(user_count):
     os.chdir('output')
     timestamp = time.strftime("%Y%m%d-%H%M%S")
     filename_csv = 'user_ids_'+timestamp+'.csv'
     filename_txt = 'user_ids_'+timestamp+'.txt'
     outputFile_csv = open(filename_csv, 'w+')
     outputFile_txt = open(filename_txt, 'w+')
     for key,value in user_count.items():
          outputFile_csv.write(key+','+str(value)+'\n')
          outputFile_txt.write(key+'\n')
     os.startfile(filename_txt)


user_ids = getSnowflakes(Tk().clipboard_get())
user_count = {}

for user_id in user_ids:
     if not user_id:
          continue
     if user_id in user_count:
          user_count[user_id] += 1
     else:
          user_count[user_id] = 1

writeResults(user_count)