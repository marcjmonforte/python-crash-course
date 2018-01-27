"""
9-5 Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3. Write a method called increment_login_attempts()
that increments the value of login_attempts by 1. Write another method called 
reset_login_attempts() that resets the value of login_attempts to 0.

Make an instance of the User class and call increment_login_attempts() 
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again
to make sure it was reset to 0.
"""

class User(object):
	def __init__(self, first_name, last_name, age, favorite_color):
		"""Initialize attributes to describe a user."""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.favorite_color = favorite_color
		self.login_attempts = 0

	def describe_user(self):
		"""Print statement describing object's attributes."""
		print "\nFirst name: " + self.first_name.title()
		print "Last name: " + self.last_name.title()
		print "User age: " + str(self.age)
		print "User favorite color: " + self.favorite_color.title()

	def greet_user(self):
		"""Print statement greeting user's full name."""
		print "\nHello, " + self.first_name.title() + " " + self.last_name.title() + "!"

	def show_login_attempts(self):
		"""Print statement showing value of login_attempts attribute."""
		print "Number of attempted logins: " + str(self.login_attempts)

	def increment_login_attempts(self):
		"""Increase login_attempts parameter value by 1."""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Reset login_attempts parameter valvue to 0."""
		self.login_attempts = 0

marc = User("marc", "monforte", 26, "gray")
marc.show_login_attempts()
marc.increment_login_attempts()
marc.increment_login_attempts()
marc.increment_login_attempts()
marc.show_login_attempts()
marc.reset_login_attempts()
marc.show_login_attempts()
