#!/usr/bin/env python3

def lowercase(password):

	return any(x.islower() for x in password)

	
def uppercase(password):

	return any(x.isupper() for x in password)

	
def length(password):

	return len(password) >= 12 


def number(password):

	return any(x.isdigit() for x in password)


def special(password):

	special_char = " !#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + '"'

	special_list = list(special_char)
	
	pass_char = list(password)

	return set(special_list).isdisjoint(set(pass_char))
	
def common_pass(password):

	f = open("password_list.txt", 'r')

	pass_list = (f.read()).split('\n')

	space = ""

	while (space in pass_list):
		pass_list.remove(space)
		
	found = password in pass_list
	
	return found

def pass_check():
	
	password = input("Enter the password: ")
	
	print ("----------------------------------")
	
	if lowercase(password) and uppercase(password) and length(password) and number(password) and not special(password) and not common_pass(password):
		print ('The password is strong!')
	else:
		print ('The password is weak!')

	if not lowercase(password):
		print ("The password should contain at least one lower case letter.")
		
	if not uppercase(password):
		print ("The password should contain at least one upper case letter.") 
	
	if not length(password):
		print ("The password should be at least 12 characters long.") 
	
	if not number(password):
		print ("The password should contain at least one number.") 
	
	if special(password):
		print ("The password should contain at least one special character.")
	
	if common_pass(password):
		print ("The password should not be a common password.") 

title = '''----------------------------------
    Password Strength Checker
----------------------------------'''
print (title)
	
pass_check()


	
	
