"""
9-13 OrderedDict Rewrite: Start with Exercise 6-4, where you used a standard
dictionary to represent a glossary. Rewrite the program using the OrderedDict
class and make sure the order of the output matches the order in which key-value
pairs were added to the dictionary.
"""

from collections import OrderedDict

vocabulary = OrderedDict()

vocabulary['a_list'] = "ordered"
vocabulary['a_dictionary'] = "key-value pairs"
vocabulary['a_tuple'] = "immutable"
vocabulary['a_int'] = "number without decimal"
vocabulary['a_float'] = "number with decminal"
vocabulary['a_string'] = "words, etc."
vocabulary['a_for_loop'] = "basic iteration through data"
vocabulary['a_while_loop'] = "loop but while condition is true"

for word, definition in vocabulary.items():
	print word.title() + ": \"" + definition.lower() + "\""