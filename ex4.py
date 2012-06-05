# -- coding: utf-8 --

# define cars value equal 100.
cars = 100

# define space in a car value equal 4.0
space_in_a_car = 4.0

# define drivers value equal 30.
drivers = 30

# define passengers value equal 90.
passengers = 90

# Calculate cars not driven value.
cars_not_driven = cars - drivers

# define cars driven value equal.
cars_driven = drivers

# Calculate carpool capacity.
carpool_capacity = cars_driven * space_in_a_car

# Calculate average passengers per car.
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."