"""
11-2 Population: Modify your function so it requires a third parameter, 
population. It should now return a single string of the form City, Country -
population xxx, such as:

Santiago, Chile - population 5000000

Run test_cities.py again. Make sure test_city_country() fails this time. 
Modify the function so the population paramater is optional. Run test_cities.py
again, and make sure test_city_country() passes again.

Write a second test called test_city_country_population() that verifies you can 
call your function with the values 'santiago', 'chile', and
'population = 5000000'. Run test_cities.py again, and make sure this new
test passes. 
"""

import unittest

def get_formatted_location(city, country, population = ''):
	"""Generate a neatly formatted city / country."""
	if population:
		formatted_location = city.title() + ", " + country.title() + \
		" - population " + population
	else:
		formatted_location = city.title() + ", " + country.title()
	return formatted_location

class LocationTestCase(unittest.TestCase):
	"""Test cases for the function 'get_formatted_location()'."""

	def test_city_country(self):
		"""Does the function return 'Santiago, Chile'?"""
		formatted_location = get_formatted_location('santiago', 'chile')
		self.assertEqual(formatted_location, 'Santiago, Chile')

	def test_city_country_population(self):
		"""Does the function return 'Santiago, Chile - population 5000000'?"""
		formatted_location = get_formatted_location('santiago', 'chile', '5000000')
		self.assertEqual(formatted_location, 'Santiago, Chile - population 5000000')

unittest.main()