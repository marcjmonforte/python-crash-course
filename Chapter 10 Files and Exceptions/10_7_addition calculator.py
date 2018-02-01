"""
10-7 Addition Calculator: Wrap your code from Exercise 10-6 
in a while loop so the user can continue to enter numbers even
if they make a mistake and enter text instead of a number.
"""

print "Let's add two numbers together!"
print "(enter 'q' to exit)\n"
while True:
	first_value = raw_input("Please enter the first number: ")
	if first_value.lower() == 'q':
		break
	second_value = raw_input("Please enter the second number: ")
	if second_value.lower() == 'q':
		break
	
	try:
		sum = int(first_value) + int(second_value)
	except ValueError:
		print "You entered something that wasn't a number!\n"
	else:
		print "The sum of " + str(first_value) + " and " + \
		str(second_value) + " is " + str(sum) + ".\n"
