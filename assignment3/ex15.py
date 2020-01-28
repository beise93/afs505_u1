#From the module sys thiss imports the function or parameter argv. Where argv returns the specific way the sript was called.
from sys import argv
#this is the expected argument, a shortcut for assigning a variable for each value in the sequence to right of the =.
script, filename = argv
#opens the entered filename
txt = open(filename)
#Gives text and the text of the file.
print(f"Here's your file {filename}:")
print(txt.read())
#instructions on which filename to input. Line 12 defines the variable file_again as the input entered.
print("Type the filename again:")
file_again = input("> ")
#txt_again is now equal to or set to open(file_again)
txt_again = open(file_again)
#Repeats the same but uses the alternative variable that is provided by the input
print(txt_again.read())
