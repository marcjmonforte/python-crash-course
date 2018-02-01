"""
10-2 Learning C: You can use the replace() method to replace
any word with a different word. Here's a quick example showing 
how to replace 'dog' with 'cat' in a sentence:

message = "I really like dogs."
message.replace('dog', 'cat')
>>> I really like cats.

Read in each line frmo the file you just created, and replace
the word Python with the name of another language, such as C. 
Print each modified line to the screen.
"""

filename = 'learning_python.txt'
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	newLine = line.replace('Python', 'cYb3r sP4c3')
	newLine = newLine.replace('e', '3')
	newLine = newLine.replace('a', '4')
	newLine = newLine.replace('o', '0')
	newLine = newLine.replace('I', '1')
	newLine = newLine.replace('u', '|_|')
	newLine = newLine.replace('t', '7')
	print newLine.strip()