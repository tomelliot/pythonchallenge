import re
sitetext = open("site.txt").read()
#p = re.compile("[A-Z]{3}[a-z][A-Z]{3}")
p = re.compile("[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]")
#m = p.match("SOME TEXT")
#print m.groups()
#m = p.finditer("SOME TEXTOTHErTEXT mOREaTEXt")
m = p.finditer(sitetext)
l = list()
for each in m:
	l.append(each.group())

for text in l:
	print text[4:5]
