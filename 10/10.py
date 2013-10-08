from pprint import pprint 
seq = [['1']]

while True:
	for i in range(32):
		member = seq[i]
		seq.append([])
		count = 1
		for j, element in enumerate(member):
			if j < len(member)-1 and element == member[j+1]:
				count += 1 
			else:
				seq[i+1].append(str(count))
				seq[i+1].append(str(element))
				count = 1
	break
for element in seq:
	print "".join(element)
print "len(a[30]) = " + str(len(seq[30]))
