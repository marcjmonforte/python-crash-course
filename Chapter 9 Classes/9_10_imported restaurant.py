"""
9-10 Imported Restaurant: Using your latest Restaurant class, store it in
a module. Make a separate file that imports Restaurant. Make a Restaurant
instance, and call one of Restaurant's methods to show that the import 
statment is working properly.
"""

import restaurant
myRestaurant = restaurant.Restaurant("burger king", "fast")
myRestaurant.describe_restaurant()