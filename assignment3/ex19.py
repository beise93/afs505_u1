# Creates a function with name 'cheese_and_crackers' with arugments 'cheese_count' and
# 'boxes_of_crackers'

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!") #Prints the value of 'cheese_count in a string using formatter'
    print(f"You have {boxes_of_crackers} boxes of crackers!") #Print the value of 'boxes_of_crackers in a string using a formatter'
    print("Man that's enough for a party!") #Prints a string
    print("Get a blanket.\n") #prints a string

#Prints a string
print("We can just give the function numbers directly:")
#Calls the function "cheese_and_crackers" with argument values of 20 and 30
cheese_and_crackers(20, 30)

#prints a string
print("OR, we can use variables from out script:")
#Creates a variable 'amount_of_cheese' with value of 10
amount_of_cheese = 10
#Cretes a varible 'amount_of_crackers' with value of 50
amount_of_crackers = 50
#Calls the function "cheese_and_crackers" with arguments set to the variables created previously
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#prints a string
print("We can even do math inside too:")
#calls the function 'cheese_and_crackers' with the arugments 10 + 20 and 5 + 6
cheese_and_crackers(10 + 20, 5 + 6)

#prints a string
print("And we can combine the two, variables and math:")
#calls the function 'cheese_and_crackers' in which the variables 'amount_of_cheese' and 'amount_of_crackers' have math operations
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
