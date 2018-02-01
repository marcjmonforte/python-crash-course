"""
10-5 Programming Poll: Write a while loop that asks people
why they like programming. Each time someone enters a reason,
add their reason to a file that stores all the responses.
"""

filename = "programming_poll.txt"
with open(filename, "a") as file_object:
	while True:
		reason = raw_input("Why do you like to program? (enter q to quit)\n")
		if reason.lower() != "q":
			file_object.write("User input: " + reason.lower() + "\n")
			print "Thanks for contributing! Your input has been recorded.\n"
		
		else:
			break