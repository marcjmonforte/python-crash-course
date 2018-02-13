"""
11-3 Employee: Write a class called Employee. The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes. Write a method called give_raise() that adds $5000 to the 
annual salary by default but also accepts a different raise amount.

Write a test case for Employee. Write two test methods,
test_give_default_raise() and test_give_custom_raise(). Use the setUp() method
so you don't have to create a new employee instance in each test method. Run your
test case, and make sure both tests pass.
"""

import unittest

class Employee(object):

	def __init__(self, first_name, last_name, annual_salary):
		self.first_name = first_name
		self.last_name = last_name
		self.annual_salary = annual_salary

	def give_raise(self, raise_amount = '5000'):
		current_salary = int(self.annual_salary)
		new_salary = current_salary + int(raise_amount)
		self.annual_salary = new_salary

class TestEmployee(unittest.TestCase):

	def setUp(self):
		self.my_employee = Employee('Marc', 'Monforte', 75000)

	def test_give_default_raise(self):
		old_salary = self.my_employee.annual_salary
		self.my_employee.give_raise()
		new_salary = self.my_employee.annual_salary

		self.assertEqual(new_salary, (old_salary + 5000))

	def test_give_custom_raise(self):
		old_salary = self.my_employee.annual_salary
		custome_raise_amount = 7500
		self.my_employee.give_raise(custome_raise_amount)
		new_salary = self.my_employee.annual_salary

		self.assertEqual(new_salary, (old_salary + custome_raise_amount))

unittest.main()