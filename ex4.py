#Set the number of cars to 100
cars = 100
#Set the amount of space in a car to 4.0, maybe 4.0 meters or 4 feet? Not sure.
space_in_a_car = 4.0
#Set the number of drivers to 30
drivers = 30
#Set the number of passengers to 90
passengers = 90
#Set the number of cars not driven to be equal to cars minus the number of drivers
cars_not_driven = cars - drivers
#Set the number of cars driven to the number of drivers
cars_driven = drivers
#Set the carpool capacity to be equal to the number of cars driven times the space in each car
carpool_capacity = cars_driven * space_in_a_car
#Calculate the average passengers by car by dividing the number of passengers by the number of cars cars_driven
average_passengers_per_car = passengers / cars_driven

#These are stats for cars, passengers, and carpooling.
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "passengers to carpool today.")
print("We need to put about", average_passengers_per_car, "passengers in each car.")
