import urllib2
import bz2
import struct
inp = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/integrity.html").readlines()
for line in inp:
	if line[0:2] == "un":
		un = bytes(line[5:-2])
	if line[0:2] == "pw":
		pw = bytes(line[5:-2])
print "user: " + bz2.decompress(un.decode("string_escape"))
print "pass: " + bz2.decompress(pw.decode("string_escape"))
