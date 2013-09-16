f = open('2.txt')
txt = f.read()
l = [0]*256
for char in txt:
	if txt.count(char) < 2:
		print char
f.close()
