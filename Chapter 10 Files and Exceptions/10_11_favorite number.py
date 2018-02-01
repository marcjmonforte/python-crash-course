"""
10-11 Favorite Number: Write a program that prompts for the user's
favorite number. Use json.dump() to store this number in a file. Write
a separate program that reads in this value and prints the message,
"I know your favorite number! It's _____."
"""

import json

def get_stored_number():
	filename = "favorite_number.json"
	try:
		with open(filename) as f_obj:
			favorite_number = json.load(f_obj)
	except:
		return None
	else:
		return favorite_number

def get_favorite_number():
	user_prompt = "Can't seem to remember what your favorite "
	user_prompt += "number is. Care to remind me what it is?\t"
	favorite_number = raw_input(user_prompt)

	filename = "favorite_number.json"
	with open(filename, 'w') as f_obj:
		json.dump(favorite_number, f_obj)

	return favorite_number

def return_favorite_number():
	favorite_number = get_stored_number()
	if favorite_number:
		print "I know your favorite number - it's " + \
			str(favorite_number) + "!"
	else:
		favorite_number = get_favorite_number()
		print "I didn't know that before, but I'll remember from " + \
		"now on that your favorite number is " + str(favorite_number) + "!"
			

return_favorite_number()