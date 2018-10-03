import sys


# sys.argv[0] = name of script



i = 0

for arg in sys.argv:
	
	i += 1
	
	print("Argument no ", i, ": ", arg)