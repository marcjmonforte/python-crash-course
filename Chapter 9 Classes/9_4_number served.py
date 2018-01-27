"""
9-4 Number Served: Start with your program from Exercise 9-1. Add an 
attribute called number_served with a default value of 0. Create an 
instance called restaurant from this class. Print the number of customers
the restaurant has served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number of 
customers that have been served. Call this method with a new number
and print the value again.

Add a method called increment_number_served() that lets you increment 
the number of customers who've been served. Call this method with any number
you like that could represent how many customers were served in, say, a 
day of business.
"""

class Restaurant(object):
	def __init__(self, restaurant_name, cuisine_type):
		""" Initiatlize attributes to describe a restaurant."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Print statement describng object's attributes."""
		print "This restaurant's name is " + self.restaurant_name.title() + \
			  " and it serves " + self.cuisine_type.title() + " food."

	def open_restaurant(self):
		"""Print statement indicating that restaurant is open."""
		print self.restaurant_name.title() + " is open!"

	def count_number_served(self):
		"""Print statement indicating number of customers served."""
		print self.restaurant_name.title() + " has served " + \
		str(self.number_served) + " customers today."

	def set_number_served(self, customer_count):
		"""Changes self.number_served attribute, then prints
		statement indicating this change."""
		self.number_served = customer_count
		self.count_number_served() 

	def increment_number_served(self, customer_count):
		"""Increments self.number_served attribute by argument, then
		prints statemnt indicating this change."""
		self.number_served += customer_count
		self.count_number_served()

restaurant = Restaurant("Din Tai Fung", "Chinese")
restaurant.count_number_served()
restaurant.set_number_served(11)
restaurant.increment_number_served(26)