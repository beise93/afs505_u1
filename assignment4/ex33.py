i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}:")


print("The numbers: ")

for num in numbers:
    print(num)

print("Study drill 1")
def studydrill1(n):
    i = 0
    numbers1 = [ ]
    while i < n:
        print(f"number: {i}")
        numbers1.append(i)
        i = i + 1
    print(numbers1)

studydrill1(4)

studydrill1(5)

print("Study drill 3 with steps in function.")
def studydrill3(n, s):
    i = 0
    numbers3 = [ ]
    while i < n:
        print(f"number: {i}")
        numbers3.append(i)
        i = i + s
    print(numbers3)

studydrill3(10, 2)

print("Study drill 5.")
def studydrill5(n, s):
    numbers5 = range(0, n, s)
    for i in numbers5:
        print(f"number: {i}")
    print(numbers5)


studydrill5(5, 1)
