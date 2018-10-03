import sys
def is_polindrome(x):
	x = x.lower()
	for i in range(len(x)//2):
		if x[i] != x[len(x)-1-i]:
			return False
			break
	return(True)
if len(sys.argv) == 1:
	x = input('Please provide with a word : ')
else:
	x = sys.argv[1]
print(is_polindrome(x))