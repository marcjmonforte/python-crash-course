"""
8-12 Sandwiches: Write a function that accepts a list of items that a 
person wants on a sandwich. The function should have one parameter that
collects as many items as the function call provides, and it should 
print a summary of the sandwich that is being ordered. Call the function
three times, using a different number of arguments each time.
"""

def make_sandwich(*toppings):
	if toppings:
		if len(toppings) == 1:
			print "Making a sandwich with only one topping:"
			for topping in toppings:
				print " - " + topping.lower()	
			print "\n"
		else:
			print "Making a sandwich with the following toppings:"
			for topping in toppings:
				print " - " + topping.lower()
			print "\n"
	else:
		print "Your sandwich has no toppings, are you sure about this?"
		print "\n"

make_sandwich()
make_sandwich("ham")
make_sandwich("ham", "mayo", "cheese", "mustard", "lettuce")