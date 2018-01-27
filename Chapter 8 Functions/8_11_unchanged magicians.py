"""
8-11 Unchanged Magicians: Start with your work from 8-10. Call the
function make_great() with a copy of the list of magicians' names. Because
the original list will be unchanged, return the new list and store it in a 
separate list. Call show_magicians() with each list to show that you have 
one list of the original names and one list with "the Great" added to each
magician's name.
"""

def show_magicians(magicians):
	for magician in magicians:
		message = "Here comes " + magician.title() + "!"
		print message

def make_great(magicians):
	while magicians:
		current_magician = magicians.pop()
		if current_magician[0:3].lower() == "the":
			message = "Here comes The Great " + current_magician[4:].title() + "!"
		else:
			message = "Here comes The Great " + current_magician.title() + "!"
		print message
		great_magicians.append(current_magician)

magicians = ["houdini", "the dark magician", "likebert", "likethebert"]
great_magicians = []

make_great(magicians[:])
print "\n"
show_magicians(magicians[:])
print "\n"

print "Here's proof that the original lists haven't been changed."
print magicians
print great_magicians