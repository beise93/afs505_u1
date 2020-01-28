#Imports argv function from the sys library
from sys import argv
#Sets argv to accept the script and 'test.txt' file as input
script, input_file = argv
#Creates a function "print_all(f)" which reads and prints the input
def print_all(f):
    print(f.read())
#creates a function 'rewind(f)' which sets the input files current position to 0 through the seek function
def rewind(f):
    f.seek(0)
#creates a function that accepts an integer. Readline() reads a single line up to the \
#n character but leaves the \n character at the end of the line
def print_a_line(line_count, f):
    print(line_count, f.readline())
#sets current_file to equal the file object input_file, which is defind in the command line when running the script
current_file = open(input_file)
#prints the whole file on a new line.
print("First let's print the whole file:\n")
#calls the function print_all using current_line
print_all(current_file)
#prints text
print("Now let's rewind, kind of like a tape.")
#calls the function rewind with the paramter current_file
rewind(current_file)
#prints text
print("Let's print three lines:")
#calls function print_a_line with current_line and current_file as parameters.
#Then current_line is incremented by 1
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
