a = int(input ("Please provide with a number : "))
f = 1
if a == 0:
	print('Factorial of 0 is 0')
else:
	for i in range(1,a+1):
		f = f*i
	print('Factorial of {} is {}'.format(a,f))