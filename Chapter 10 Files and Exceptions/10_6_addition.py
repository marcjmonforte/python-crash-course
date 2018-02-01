"""
10-6 Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you'll get a ValueError. Write a program that prompts
for two numbers. Add them together and print the result. Catch the
ValueError if either input is not a number, and print a friendly error 
message. Test your program by entering two numbers and then by entering
some text instead of a number.
"""

def add_numbers(first_value, second_value):
	"""Adds two numbers together."""
	try:
		sum = int(first_value) + int(second_value)
	except ValueError:
		print "You entered something that wasn't a number!"
	else:
		print "The sum of " + str(first_value) + " and " + \
		str(second_value) + " is " + str(sum) + "."
		return sum

add_numbers(1, 2)
add_numbers(-1, -3)
add_numbers(0, 0)
add_numbers(1, "blue")
add_numbers("blue", 1)