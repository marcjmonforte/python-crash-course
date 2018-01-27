"""
9-7 Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 or 9-5.
Add an attribute, privileges, that stoers a list of strings like "can
add post", "can delete post", "can ban user", and so on. Write a method called 
show_privileges() that lists the administrator's set of privlieges. Create
an instance of Admin, and call your method.
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

class Admin(User):
	def __init__(self, first_name, last_name, age, favorite_color):
		"""Create subclass of User parent class."""
		super(Admin, self).__init__(first_name, last_name, age, favorite_color)
		self.privileges = ["can add post", 
						   "can delete post", 
						   "can ban user",]

	def show_privileges(self):
		"""Print values for self.privleges."""
		print "Admin's have the following perks: "
		for privilege in sorted(self.privileges):
			print " * " + privilege

marc = Admin("marc", "monforte", 27, "gray")
marc.show_privileges()