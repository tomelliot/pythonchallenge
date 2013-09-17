import urllib2
import pickle
import pprint
inp = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
outp = pickle.load(inp)
inp.close()

for l in outp:
	line = [char * nb for char, nb in l] 
	print "".join(line)
