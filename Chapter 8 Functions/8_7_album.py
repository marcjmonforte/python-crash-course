"""
8-7 Album: Write a function called make_album() that builds a 
dictionary describe a music album. THe function should take in an 
artist name and an album title, and it should return a dictionary
containing these two pieces of information. Use the function to 
make three dictionaries representing different albums. Print each return
value to show that the dictionaries are storing the album information 
correctly.

Add an optional parameter to make_album() that allows you to store
the number of tracks on an album. If the calling line includes a value 
for the number of tracks, add that value to the album's dictionary. 
Make at least one new function call that includes the number of 
tracks on an album.
"""

def make_album(artist_name, album_title):
	album = album_title.title() + " by " + artist_name.title()
	print album

make_album("Bruno Mars", "24K Magic")
make_album("TWICE", "Twicetagram")
make_album("N.E.R.D", "No One Ever Really Dies")

def make_album(artist_name, album_title, track_count = ''):
	if track_count:
		album = artist_name.title() + " has released an album called " + \
				album_title.title() + ". The album has " + str(track_count) + \
				" songs in total."
	else:
		album = artist_name.title() + " has released an album called " + \
				album_title.title() + "."
	print album

make_album("Bruno Mars", "24K Magic", 10)
make_album("Bruno Mars", "24K Magic")