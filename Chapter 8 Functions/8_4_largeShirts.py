"""
8-4 Large Shirts: Modify the make_shirt() function so that shirts 
are large by default with a message that reads I Love Python. Make a 
large shirt and a medium shirt with the default message, and a shirt of
any size with a different message.
"""

def make_shirt(size = "large", text = "I Love Python"):
	print "You have requested a " + size.lower() + \
		" shirt.\nThe shirt has text on it that says: \"" + \
		text.capitalize() + ".\""

make_shirt()
make_shirt(size = "medium")
make_shirt(size = "small", text = "python is cool")