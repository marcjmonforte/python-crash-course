"""
10-4 Guest Book: Write a while loop that prompts users for 
their name. When they enter their name, print a greeting to 
the screen and add a line recording their visit in a file called
guest_book.txt. Make sure each entry appears on a new line in 
the file.
"""

filename = "guest_book.txt"
with open(filename, 'a') as file_object:
	while True:
		register = raw_input("Would you like to register a new guest? (y\\n)\t")
		if register != "n":
			first_name = raw_input("What is your first name?\t")
			last_name = raw_input("And what is your first name?\t")
			print "Thank you. Your name has been registered."
			print "Welcome to the party, " + first_name.title() + " " + \
				last_name.title() + "!\n"

			file_object.write("Guest Name: " + first_name.lower() + " " + \
				last_name.lower() + "\n")

		else:
			break