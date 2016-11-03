import re

f = open('0009603','r')
fileText = f.read()
tofind = re.compile('\d\d\d\d\d\d\d\d\d\d')
match = re.findall(tofind,fileText)
for u in match:
	print str(u)

