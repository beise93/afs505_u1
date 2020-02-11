## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## class Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## class Dog has a __init__ that takes self and name as params
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)
    @staticmethod
    def make_dog_noise(self):
        print('Baark!')

Atlas = Dog(Animal)
Atlas.dogspecies = "Newfoundland"

print(Atlas.dogspecies)


 ## class Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## class Cat has a __init__ that takes self and name as params
        self.name = name
    def make_cat_noise():
        print("Meow!")
Felix = Cat(Animal)
Sam = Cat(Animal)
Felix.color = 'tabby'
Sam.color = 'black'

Felix.size = 'portly'
Sam.size = 'chubby'


print(Felix.color)
print(Sam.size)


## class Person is-a object
class Person(object):

 def __init__(self, name):
 ## class person has a __init__ that takes self and name as params
    self.name = name

 ## Person has-a pet of some kind
    self.pet = None

 ## class Employee is a Person
class Employee(Person):

    def __init__(self, name, salary):
## ?? hmm what is this strange magic?
##
        super(Employee, self).__init__(name)
## Employe has-a salary attribute
        self.salary = salary

 ## Fish is-a object
class Fish(object):

    def __init__(self, species):

        self.species = species

 ## Salmon is-a Fish
class Salmon(Fish):
    def __init__(self, species, size):
        super(Salmon, self).__init__(species)


 ## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is a Person
mary = Person("Mary")

## sets pet attribute of mary to satan
mary.pet = satan
print(mary.pet)
## frank has-a attributes of Frank and salary of 120000
frank = Employee("Frank", 120000)

## sets pet attribute of frank to rover
frank.pet = rover
print(frank.salary)
## flipper is-a fish
flipper = Fish("Halibut")

## crous is-a salmon
crouse = Salmon("Chinook", "large")
print(crouse.species)
## harry is-a halibut
harry = Halibut("Atlantic")
George = Person(object)
George.name = "George Berkeley"
print(George.name)
{
"Juventus": ["Ronaldo", "Dybala"],
"Inter": ["Sanchez", "Lukaku"],
"Milan": ["Ibrahimovic"]
}
