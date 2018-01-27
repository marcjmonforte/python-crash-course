"""
9-6 Ice Cream Sandwich: An ice cream stand is a specific kind of 
restaurant. Write a class called IceCreamStand that inherets from the 
Restaurant class that you wrote in Exercise 9-1 or 9-4. Either version 
of the class will work; just pick the one you like better. Add an 
attribute called flavors that stores a list of ice cream flavors.
Write a method that displays these flavors. Create an instance of 
IceCreamStand, and call this method.
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

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		"""Create subclass of Restaurant parent class."""
		super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
		self.flavors = ['vanilla', 'chocolate', 'strawberry', 'coffee']

	def display_flavors(self):
		"""Print values for self.flavors attribute."""
		print "Here at " + self.restaurant_name.title() + ", we serve " + \
		"the following flavors: "
		for flavor in sorted(self.flavors):
			print " * " + flavor.title()

iceCream = IceCreamStand("Mocha Joe", "ice cream")
iceCream.display_flavors()