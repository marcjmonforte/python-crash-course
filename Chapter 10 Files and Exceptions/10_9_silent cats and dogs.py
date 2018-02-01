"""
10-9 Silent Cats and Dogs: Modify your except block in Exercise
10-8 to fail silently if either file is missing.
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
		pass
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
