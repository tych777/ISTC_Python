list1 = [3, 6, True, True, -1, "abc", (1, 2), [2, 3], 6]
for i in range(len(list1)):
	if type(list1[i]) is tuple:
		print('Index of a first tuple is', i)
		break