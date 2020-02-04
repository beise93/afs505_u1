

print("If the weather is nice do you want to go on a walk?")
def get_on_with_it():
    print("Let's get on with it then.")
    print("Where should we talk a walk to?")
    places = ['countryside', 'town square', 'market']
    print(places)

choice = input("> ")

if "yes" in choice:
    get_on_with_it()
elif "no" in choice:
    print("Better off enjoying tea.")
else:
    print("I do not know let's see.")


def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

shoes = {'name': 'Fancy Shoes', 'price': 14900}

print(apply_discount(shoes, 0.25))

x = 2

if x < 0:
    raise Exception("Number is less than zero.")


def examplefunc():
    yield 1
    yield 2
    yield 3
""" Looking yield up: 'Return sends a specified value back to its caller whereas Yield can produce a sequence of values.
We should use yield when we want to iterate over a sequence,
 but don’t want to store the entire sequence in memory'."""

# Driver code to check above generator function
for value in examplefunc():
    print(value)
