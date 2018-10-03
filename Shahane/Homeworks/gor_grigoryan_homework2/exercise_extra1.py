while True:
	password = input('Input Password : ')
	if len(password) < 8:
		print('Invalid Password !!!')
	elif password.isdigit():
		print('Invalid Password !!!')
	elif password.lower() == password:
		print('Invalid Password !!!')
	else:
		print("Welcome !!!")
		break