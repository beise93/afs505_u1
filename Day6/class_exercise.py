def main():
    from sys import argv
    script, filename = argv
    filehandle = open(filename)
    count = 0
    line = filehandle.readline()
    while line:
        count += 1
        line = filehandle.readline()
    

    file = open(filename)
    data = file.read()
    words = data.split()


    file = open(filename)
    data = file.read()
    number_of_characters = len(data)

    print(count, len(words), number_of_characters, filename)




main()
