"""
9-14 Dice: The module random contains a function that generates random
numbers in a variety of ways. The function randint() returns an integer
in the range you provide. The following code returns a number between
1 and 6:

from random import randint
x = randint(1, 6)

Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and 
roll it 10 times.
"""

from random import randint

class Die(object):
	def __init__(self, sides = 6):
		self.sides = sides

	def roll_die(self):
		"""Rolls a random number between one and number of sides."""
		roll_result = randint(1, self.sides)
		print "You rolled a " + str(roll_result) + "."


myDice = Die()
attemptCount = 1
while attemptCount < 11:
	print "Attempt #" + str(attemptCount)
	myDice.roll_die()
	attemptCount += 1
