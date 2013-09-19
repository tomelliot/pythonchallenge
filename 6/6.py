import string
from zipfile import ZipFile as z
fileNb = ""
nextFileNb = "90052"
directory = "./channel/"
extension = ".txt"
comments = ""
#with open("./dir.txt") as f:
#	for line in f:
#		print open("./channel/" + "".join(s for s in line if s not in string.whitespace)).read()

zf = z("channel.zip")
while fileNb <> nextFileNb:
	fileNb = nextFileNb
	comments += zf.getinfo(fileNb + extension).comment
	f = open(directory + fileNb + extension)
	fileText = f.read()
	nextFileNb = fileText.split()[-1]
	print fileText + " (" + nextFileNb + ")"
	if nextFileNb == "comments.":
		break
print comments
