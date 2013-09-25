from PIL import Image
import sys
i = Image.open("oxygen.png")
a = ""
b = ""
convert = False
#for line in i.getdata():
#	print list(line)
o = i.crop([0, 45, 607, 46])
for pixel in list(o.getdata())[0::7]:
	a += chr(pixel[1])
sys.stdout.write(a)
#o.save("/var/www/downloads/oxygen.png")
print ":"
for letter in a:
	if convert == True:
		if letter == ',' or letter == ']':
			sys.stdout.write(chr(int(b)))
			#print chr(int(b))
			b = ""
		else:
			b += letter
	if letter == '[':
		convert = True
print "!"
