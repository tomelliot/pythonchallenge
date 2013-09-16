import urllib2
baseurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothingnum = "12345"
nothingnum = "61827"
lastnothingnum = ""
while nothingnum <> lastnothingnum:
	lastnothinignum = nothingnum
	sitedata = urllib2.urlopen(baseurl+nothingnum).read()
	nothingnum = sitedata.split()[-1]
	print nothingnum, sitedata
