"""
8-6 City Names: Write a function called city_country() that takes in the 
name of a city and its country. The function should return a string formatted
like this: "Santiago, Chile". Call your own function wiht at least three city-
country pairs, and print the value that's returned.
"""

def city_country(city, country):
	formatted_cityCountry = '"' + city.title() + ", " + country.title() + '"'
	print formatted_cityCountry

city_country("San Jose", "United States")
city_country("Tokyo", "Japan")
city_country("Seoul", "South Korea")