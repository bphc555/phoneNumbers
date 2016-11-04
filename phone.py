import re
import os
from os.path import isfile

def getPhone(name):
	f = open(name,'r')
	fileText = f.read()
	tofind = re.compile("\D([0]?\d{10})\D") #phone numbers like 09874563210 or 9874563210 or 91-9874563210
	match = re.findall(tofind,fileText)
	for u in match:
		print  str(u)
	
	tofind2 = re.compile("\D(91\d{10})\D") #phone numbers like 919874563210
	match = re.findall(tofind2,fileText)
	for u in match:
		print  str(u)
	

#directory = '/home/sonal/Desktop/myDir'

def recurse(dirName):
	for subdir, dirs, files in os.walk(dirName):
		for fileName in files:
		 	path = os.path.join(subdir, fileName)
			getPhone(path)

def main():
	print "Enter the path to your directory"
	directory = raw_input()
	print "you entered - " + directory
	print "The phone numbers found are: "
	recurse(directory)

main()
