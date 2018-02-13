"""
11-1 City, Country: Write a function that accepts two parameters: a
city name and a country name. THe function should return a single string of the form
City, Country, such as Santiago, Chile. Store the function in a module called
city_functions.py.

Create a file called test_cities.py that tests the functions you just wrote 
(remember that you need to import unittest and the function you want to test).
Write a method called test_city_country() to verify that calling your function 
with values such as 'santiago' and 'chile' result in the correct string. Run 
test_cities.py, and make sure test_city_country() passes.
"""

import unittest

def get_formatted_location(city, country):
	"""Generate a neatly formatted city / country."""
	formatted_location = city + ", " + country
	return formatted_location.title()

class LocationTestCase(unittest.TestCase):
	"""Test cases for the function 'get_formatted_location()'."""

	def test_get_formatted_location(self):
		"""Does the function return 'Seoul, South Korea'?"""
		formatted_location = get_formatted_location('seoul', 'south korea')
		self.assertEqual(formatted_location, 'Seoul, South Korea')

unittest.main()