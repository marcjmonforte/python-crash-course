"""
9-9 Battery Upgrade: Use the final version of electric_car.py from this 
section. Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capactiy to 85 if it isn't already.
Make an electric car with a default battery size, call get_range() once, and
then call get_range() a second time after upgrading the battery. You should see 
an increase in the car's range.
"""

class Car(object):
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make
		long_name += ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print "This car has " + str(self.odometer_reading) + \
		" miles on it."

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print "You can't roll back an odometer!"

class Battery(object):
	def __init__(self, battery_size = 70):
		self.battery_size = battery_size

	def describe_battery(self):
		print "This car has a " + str(self.battery_size) + \
		"-kWh battery."

	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print message

	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85
		else:
			print "Battery already at maximum capacity."

class ElectricCar(Car):
	def __init__(self, make, model, year):
		super(ElectricCar, self).__init__(make, model, year)
		self.battery_size = Battery()

myCar = ElectricCar("Tesla", "Model 3", 2018)
print myCar.get_descriptive_name()
myCar.battery_size.get_range()
myCar.battery_size.upgrade_battery()
myCar.battery_size.get_range()
myCar.battery_size.upgrade_battery()