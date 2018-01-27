"""
8-3 T-Shirt: Write a function called make_shirt() that accepts a size and 
the text of a message that should be printed on the shirt. The function 
should print a sentence, summarizing the size of the shirt and the message
printed on it. 

Call the function once using positional arguments to make a shirt. Call
the function a second time using keyword arguments.
"""

def make_shirt(size, text):
	print "You have requested a " + size.lower() + \
		" shirt.\nThe shirt has text on it that says: \"" + \
		text.capitalize() + ".\""

make_shirt("medium", "this shirt is medium")
make_shirt(size = "medium", text = "this shirt is medium")