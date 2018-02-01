"""
10-8 Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least
three names of cats in the first file and three names of dogs in the second
file. Write a program that tries to read these files and print the contents 
of the file to the screen. Wrap your code in a try-except block to catch the
FileNotFound error, and print a friendly message if a file is missing. Move
one of the files to a different location on your system, and make sure the code 
in the except block executes properly.
"""

cat_file = "animals/cats.txt"
dog_file = "animals/dogs.txt"
lizard_file = "animals/lizard_file.txt"

def read_file_contents(filename):
	"""Read and prints text within file."""
	try:
		with open(filename) as file_object:
			content_list = file_object.readlines()
	except:
		error_msg = "ERROR: File \"" + filename + "\" cannot be found."
		print error_msg
	else:
		for item in content_list:
			if item == content_list[-1]:
				print item.strip()
			else:
				formated_item = item.strip() + ", "
				print formated_item,

read_file_contents(cat_file)
read_file_contents(lizard_file)
read_file_contents(dog_file)
