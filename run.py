#!/usr/bin/env python
#Code by Nikhil Kumar
#https://in.linkedin.com/in/nikhil-kumar-4b9443166
import os
import subprocess 

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m".format(skk))

path = raw_input ("Path of your Domain and Subdomain List: ")
output_file = raw_input("Save your Output: ")
if output_file != "":
	file1 = open(output_file, 'w')
	file1.close() 
	prRed("\n" + path )

#opening file
file = open(path, 'r')
count = 0

for line in file:
	count +=1
	domain = "{}".format(line.strip()) 
	text = "\n+-----------------------------------------------------------------+" + "\n[.] Start Fetching Informtion " + domain + "\n+-----------------------------------------------------------------+\n"
	prGreen(text)	
	cmd = "whatweb " + domain	
	#cmd_result = str(os.system(cmd + domain))
	cmd_result = subprocess.check_output(cmd, shell=True)
	print(str(cmd_result))

	if output_file != "":
		#Writting to file
		file1 = open(output_file, 'a') 
		file1.write(text) 
		file1.write(str(cmd_result)) 
		file1.close() 

file.close()

