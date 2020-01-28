from sys import argv

script, filename = argv

with open(filename) as f:
    output = f.read()
