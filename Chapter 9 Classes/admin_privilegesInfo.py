from userInfo import User

class Privileges(object):
	def __init__(self):
		self.privileges = ["can add post", "can delete post", "can ban user",]

	def show_privileges(self):
		"""Print values for self.privleges."""
		print "Admin's have the following perks: "
		for privilege in sorted(self.privileges):
			print " * " + privilege

class Admin(User):
	def __init__(self, first_name, last_name, age, favorite_color):
		"""Create subclass of User parent class."""
		super(Admin, self).__init__(first_name, last_name, age, favorite_color)
		self.privileges = Privileges()