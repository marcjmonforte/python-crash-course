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

