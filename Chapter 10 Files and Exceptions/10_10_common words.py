"""
10-10 Common Words: Visit Project Gutenberg (http://gutenberg.org/)
and find a few texts you'd like to analyze. Download the text files
for these works, or copy the raw text from your browser into a text
file on your computer.

You can use the count() method to find out how many times a word or
phrase appears in a string. For example, the following code counts the 
number of times 'row' appears in a string:

line = "Row, row, row your boat"
line.count("row")
>> 2

line.lower().count("row")
>> 3

Notice that converting the string to lowercase using lower() catches
all appearances of the word you're looking for, regardless of how it's 
formatted.

Write a program that reads the files you found at Project Gutenberg
and determine how many times the word 'the' apperas in each text.
"""

def count_words(filename, word):
	"""Count the number of times a word appears in a given file."""
	try:
		with open(filename) as file_object:
			content = file_object.readlines()
	except:
		print "The file \"" + filename[11:] + "\" cannot be found."
	else:
		content = "".join(content)
		total_count = content.lower().count(word)
		print "The word \"" + word.lower() + "\" appears " + \
		str(total_count) + " times in the file \"" + filename[11:] + "\"."

nunnery_life = "book_files/nunnery_life.txt"
the_great_pearl_secret = "book_files/the_great_pearl_secret.txt"
an_act_in_the_backwater = "book_files/an_act_in_the_backwater.txt"
poo_poo_time = "book_files/poo_poo_time.txt"

count_words(nunnery_life, "the")
count_words(the_great_pearl_secret, "the")
count_words(poo_poo_time, "the")
count_words(an_act_in_the_backwater, "the")