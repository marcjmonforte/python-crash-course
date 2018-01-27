"""
8-8 User Albums: Start with your program from 8-7. Write a 
while loop that allows users to enter an album's artist and
title. Once you have that information, call make_album() with
the user's input and print the dictionary that's created. Be 
sure to include a quit value in the while loop.
"""

def make_album(artist_name, album_title, track_count = ''):
	if track_count:
		album = artist_name.title() + " has released an album called " + \
				album_title.title() + ". The album has " + str(track_count) + \
				" songs in total."
	else:
		album = artist_name.title() + " has released an album called " + \
				album_title.title() + "."
	return album

print "Let's format some albums!"
print "(enter 'q' at any time to quit)"

while True:
	artist = raw_input("What is the artist's name?   ")
	if artist.lower() == 'q':
		break

	album = raw_input("What is the name of their album?   ")
	if album.lower() == 'q':
		break


	print make_album(artist, album) + "\n"
