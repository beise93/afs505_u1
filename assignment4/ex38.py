ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
            "Corn", "Banana", "Girl", "Boy"]


while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")
print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:5])) # super stellar!


# Study drill 6

seriea_teams = ["Juve", "Inter", "Lazio", "Roma", "Atalanta", "Cagliari", "Parma", "Milan", "Bologna", "Verona"]
print(seriea_teams[2:5])

for x in seriea_teams:
    print(x)

if "Juve" in seriea_teams:
    print("Yes, 'Juve' is in this list")

print(len(seriea_teams))
