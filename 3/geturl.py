import urllib2
url = "http://www.pythonchallenge.com/pc/def/equality.html"
f = open("site.txt", "w")
sitedata = "".join([line.rstrip("\n") for line in urllib2.urlopen(url).readlines()])
out = sitedata.split("--")
f.write(out[len(out)-2])

