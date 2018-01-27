"""
8-10 Great Magicians: Start with a copy of your program from
Exercise 8-9. Write a function called make_great() that modifies the list
of magicians by adding the phrase "the Great" to each magician's name. 
Call show_magicians() to see that the list has actually been modified. 
"""

def make_great(magicians):
	for magician in magicians:
		if magician[0:3].lower() == "the":
			message = "Here comes the great " + magician[4:].title() + "!"
		else:
			message = "Here comes the great " + magician.title() + "!"
		print message

magicians = ["houdini", "the dark magician", "likebert", "likethebert"]
make_great(magicians)