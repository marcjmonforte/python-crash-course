"""
9-1 Restaurant: Make a class called Restaurant. The __init__()
method for Restaurant should store two attributes: a restaurant_name
and a cuisine_type. Make a method called describe_restaurant()
that prints these two pieces of information, and a method called 
open_restaurant() that prints a message indicating that the 
restaurant is open.

Make an instance called restaurant from your class. Print the two
attributes individually, then call both methods. 
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

restaurant = Restaurant("cheesecake factory", "american")
restaurant.describe_restaurant()
restaurant.open_restaurant()