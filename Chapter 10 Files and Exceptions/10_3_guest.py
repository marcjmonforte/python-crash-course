"""
10-3 Guest: Write a program that prompts the user for their name. 
When they respond, write their name to a file called guest.txt.
"""

filename = 'guest.txt'
with open(filename, 'a') as file_object:
	first_name = raw_input("What is your first name?\t")
	last_name = raw_input("And what is your first name?\t")
	print "Thank you. Your name has been registered."

	file_object.write("Guest Name: " + first_name.lower() + " " + \
		last_name.lower() + "\n")