import sys
import divisors
def prime_num_checker(x):
	s = divisors.divisors(x)
	if len(s) == 2 or len(s) == 1:
		return True
	else:
		return False
if len(sys.argv) == 1:
	x = int(input('Please provide with a number : '))
else:
	x = int(sys.argv[1])
print(prime_num_checker(x))