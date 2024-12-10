#!python3
# Read the contents of a file that has a json encoded list of numbers.
# Find the largest number in each list
# task01a: 63545
# task01b: 63876
# task01c: 63891

import json

def larges(file):
    largest = 0
    filename = file
    filer = open(filename,"r")
    data = filer.read()
    decoded = json.loads(data)
    
    for i in range(len(decoded)):
        if decoded[i] > largest:
            largest = decoded[i]
    print(largest)
    return largest

larges('task01a.txt')
larges('task01b.txt')
larges('task01c.txt')