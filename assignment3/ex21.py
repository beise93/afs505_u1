def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

study3 = add(age, multiply(weight, subtract(height, divide(iq, 2))))

print(study3)

print("Study drill 4.")

lemonbars = divide(30, 2)
conchas = multiply(6, 8)
brownies = add(15, 6)
pies = subtract(20, 7)

bakedgoods = subtract(conchas, add(lemonbars, multiply(brownies, divide(pies, 4))))

print(bakedgoods)
