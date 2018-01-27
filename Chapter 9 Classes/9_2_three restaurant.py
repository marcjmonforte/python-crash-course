"""
9-2 Three Restaurants: Start with your class from 9-1. Create three 
different instances from the class, and call describe_restaurant()
for each instance. 
"""

class Restaurant(object):
	def __init__(self, restaurant_name, cuisine_type):
		""" Initiatlize attributes to describe a restaurant."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Print statement describng object's attributes."""
		print "This restaurant's name is " + self.restaurant_name.title() + \
			  " and it serves " + self.cuisine_type.title() + " food."

	def open_restaurant(self):
		"""Print statement indicating that restaurant is open."""
		print self.restaurant_name.title() + " is open!"

first_restaurant = Restaurant("cheesecake factory", "american")
first_restaurant.describe_restaurant()

second_restaurant = Restaurant("din tai fung", "chinese")
second_restaurant.describe_restaurant()

third_restaurant = Restaurant("bestia", "italian")
third_restaurant.describe_restaurant()