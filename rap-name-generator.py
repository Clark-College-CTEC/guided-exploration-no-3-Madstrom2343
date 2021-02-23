# Guided Exploration No. 3
# Luke Maddison

# imports the random library
import random

# creates the lsit of possible names
possible_names = []

# opens (& creates) the rap-names-output text file, in order to begin writing in it
outputFile = open('rap-names-output.txt', 'w')

# creates a loop that is able to be read & is used to do stuff with
with open('rap-names.txt', 'r') as dataFile:
    # loops for every name in the list
    for name in dataFile:
        # appends the names to the list, taking away the line space with the rstrip
        possible_names.append(name.rstrip())

# creates a variable equal to the number of names the user wants to create
count = int(input('How many rap names would you like to create? '))
# creates a variable equal to the number of parts in a given name
parts = int(input('How many parts should the name contain? '))

# creates a loop for the amount of names the user wanted (using count)
for i in range(count):
    # begins the list for the amount of name parts
    name_parts = []
    # another loop for each part of the rap name
    for j in range(parts):
        # appends random parts from the rap names.txt & puts them together
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])
        # adds all the names together with a space & an empty line feed to the .txt file
        outputFile.write(f"{' '.join(name_parts)}\n")
        # prints out the name & adds a space
        print(f"{' '.join(name_parts)}")

# closes the rap name text file
outputFile.close()
