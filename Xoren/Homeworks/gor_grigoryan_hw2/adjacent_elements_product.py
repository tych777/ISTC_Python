import sys
def adjacent_elements_product(x):
	x = x.replace(' ','')
	print(x)
	l = []
	b = -1		
	for i in range(len(x)):
		if x[i] == ',':
			print(x[i])
			l.append(float(x[b+1:i]))
			b = i
	l.append(float(x[b+1:]))
	print(l)
	p = l[0]*l[1]
	for j in range(1,(len(l)-1)):
		if l[j]*l[j+1] > p:
			p = l[j]*l[j+1]
	return p
if len(sys.argv) == 1:
	x = input('Please provide with a comma separated list : ')
else:
	x = sys.argv[1]
print(adjacent_elements_product(x))