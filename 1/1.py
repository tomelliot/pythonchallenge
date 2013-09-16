import string
char1 = 'K'
char2 = 'M'
offset = ord(char2) - ord(char1)

#inputtext = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
inputtext = "map"
outputtext = ""
intab = ""
outtab = list()
for i in range(256):
	outtab += chr(i)
	intab += chr(i)
for i in range(ord('a'), ord('z')+1):
	if i <= ord('z')-offset:
		outtab[i] = chr(i+offset)
	else:
		outtab[i] = chr(ord('a') + (i - (ord('z')-offset))-1)
conversiontable = string.maketrans(intab,"".join(outtab))

print inputtext.translate(conversiontable)
