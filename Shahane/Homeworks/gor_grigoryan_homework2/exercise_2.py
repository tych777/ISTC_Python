from getpass import getpass
cor_username = 'Batman'
cor_pass = "I am Batman"
while True:
	inp_username = input("Input Your Username : ")
	if cor_username != inp_username:
		print('Wrong Username !!!')
		continue
	else:
		break
while True:
	inp_pass = getpass("Input Your Password : ")
	if cor_pass == inp_pass:
		print('Welcome !!!')
		break
	else:
		print('Wrong Password !!!')