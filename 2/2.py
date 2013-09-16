f = open('2.txt')
txt = f.read()
l = [0]*256
for char in txt:
	l[ord(char)] += 1
f.close()
print(l)
for i in range(len(l)):
	if l[i] == 1:
		print chr(i)
