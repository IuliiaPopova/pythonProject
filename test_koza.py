import fileinput

for line in fileinput.input(files ='akaban.txt'):
    print(line)

import fileinput

inputData = ''

for line in fileinput.input():
    inputData += line


def codeHere():
    # Use the function to return the solution.
    return inputData


print(codeHere())