"""
8-5 Cities: Write a function called describe_city() that accepts the 
name of a city and its country. The function should print a simple sentence,
such as Reykjavik is in Iceland. Give the parameter for the country a
default value. Call your function for three different cities, at at least one
of which is no the default country.
"""

def describe_city(city, country = "United States"):
	print city.title() + " is in " + country.title() + "."

describe_city("San Jose")
describe_city(city = "Los Angeles")
describe_city("Tokyo", "Japan")