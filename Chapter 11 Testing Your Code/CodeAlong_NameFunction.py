import unittest

def get_formatted_name(first, last, middle = ''):
	"""Generate a neatly formatted full name."""
	if middle:
		full_name = first + ' ' + middle + ' ' + last
	else:
		full_name = first + ' ' + last
	return full_name.title()

"""
print "Enter 'q' at any time to quit"
while True:
	first = raw_input("\nPlease give me a first name:\t")
	if first == 'q':
		break
	last = raw_input("Please give me a last name:\t")
	if last == 'q':
		break

	formatted_name = get_formatted_name(first, last)
	print "\tNeatly formatted name: " + formatted_name + "."
"""

class NamesTestCase(unittest.TestCase):
	"""Tests for 'get_formatted_name()'."""

	def test_first_last_name(self):
		"""Do names like 'Janis Joplin' work?"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')

	def test_first_last_middle_name(self):
		"""Do names like 'Wolfgang Amadeus Mozart' work?"""
		formatted_name = get_formatted_name(
			'wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()