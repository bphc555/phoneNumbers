import re
import os
from os.path import isfile

def getPhone(name):
	f = open(name,'r')
	fileText = f.read()
	tofind = re.compile('\d\d\d\d\d\d\d\d\d\d')
	match = re.findall(tofind,fileText)
	for u in match:
		print "+91-" + str(u)


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
