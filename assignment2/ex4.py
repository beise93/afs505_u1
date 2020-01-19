#assigns 100 to cars
cars = 100
#assigns space_in_a_car to 4.0
space_in_a_car = 4.0
#assings 30 to drivers
drivers = 30
#assings 90 to passengers
passengers = 90
#gives number of cars_not_driven
cars_not_driven = cars - drivers
#gives number of cars_driven
cars_driven = drivers
#yields carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
#yields average_passengers_per_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers,"drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
    "in each car.")
