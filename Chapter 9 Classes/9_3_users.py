"""
9-3 Users: Make a class called user. Create two attributes called first_name
and last_name, and then create several other attributes that are typically
stored in a user profile. Make a method called describe_user() that prints
a summary of the user's information. Make another method called greet_user()
that prints a personalized greeting to the user. 

Create several instances representing different users, and call both methods
for each user.
"""

class User(object):
	def __init__(self, first_name, last_name, age, favorite_color):
		"""Initialize attributes to describe a user."""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.favorite_color = favorite_color

	def describe_user(self):
		"""Print statement describing object's attributes."""
		print "\nFirst name: " + self.first_name.title()
		print "Last name: " + self.last_name.title()
		print "User age: " + str(self.age)
		print "User favorite color: " + self.favorite_color.title()

	def greet_user(self):
		"""Print statement greeting user's full name."""
		print "\nHello, " + self.first_name.title() + " " + self.last_name.title() + "!"

marc = User("marc", "monforte", "26", "gray")
heidi = User("heidi", "ro", "28", "red")
conan = User("conan", "O'Brian", "35", "orange")

marc.describe_user()
heidi.describe_user()
conan.describe_user()

marc.greet_user()
heidi.greet_user()
conan.greet_user()