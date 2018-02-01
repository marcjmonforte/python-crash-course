"""
10-13 Verify User: The final listing for remember_me.py assumes either
that the user has already entered their username or that the program is 
running for the first time. We should modify it in case the current user 
is not the person who last used the program.

Before printing a welcome back message in greet_user(), ask the user if 
this is the correct username. If not, call get_new_username() to get the
correct username.
"""

import json

def get_stored_username():
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except:
		return None
	else:
		return username

def get_new_username():
	username = raw_input("What is your user name?	")
	filename = "username.json"
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	username = get_stored_username()
	if username:
		confirm_user = "Hello, are you " + username + "?	(y\\n)\t"
		current_user = raw_input(confirm_user)
		if current_user.lower() == "y":
			print "Welcome back, " + username + "!"
		else:
			print "\nLooks like someone else was previously logged in."
			username = get_new_username()
			print "We'll remember you when you come back, " + \
			username + "!"
	else:
		username = get_new_username()
		print "We'll remember you when you come back, " + \
		username + "!"

greet_user()