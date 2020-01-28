name = 'Zed A. Shaw'
age = 35 # not a [ if condition else value for value in variable]
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
pounds = 180
kilos = pounds * .45359237
print("%r pounds equals %r kilos." % (pounds, kilos))
inches = 74
centimeters = inches * 2.54
print("%r inches equals %r centimeters." % (inches, centimeters))

print("pounds equals kilos." % (pounds, kilos))
