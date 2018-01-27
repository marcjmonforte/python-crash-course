"""
8-9 Magicians: Make a list of magician's name. Pass the list to 
a function called show_magicians(), which prints the name of each 
magician in the list.
"""

def show_magicians(magicians):
	for magician in magicians:
		message = "Here comes " + magician.title() + "!"
		print message

magicians = ["the great houdini", "the dark magician", "likebert"]
show_magicians(magicians)