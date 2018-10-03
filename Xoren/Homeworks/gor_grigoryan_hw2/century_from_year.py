import sys
def century_from_year(x):
	return (x+99)//100
if len(sys.argv) == 1:
	x = int(input('Please provide with a year : '))
else:
	x = int(sys.argv[1])
print(century_from_year(x))