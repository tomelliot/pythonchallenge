import urllib2
inp = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png").read()
fo = open("oxygen.png", "w")
fo.write(inp)
fo.close()
