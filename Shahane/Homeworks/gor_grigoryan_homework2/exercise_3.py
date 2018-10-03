a = [4*[0] for i in range(4)]
#a = [[0 for i in range(4)] for i in range(4)] # alternative way to create a list
for i in range(4):
	for j in range(4):
		if i == j:
			a[i][j] = 1
		else:
			a[i][j] = 2
	print(a[i])