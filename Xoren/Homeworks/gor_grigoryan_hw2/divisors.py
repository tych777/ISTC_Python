def divisors(x):
	l = []
	for i in range(1,x+1):
		if x%i == 0:
			l.append(i)
	return l