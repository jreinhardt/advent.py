"""
0x02

Dictionaries
============

Dictionaries are a data structure to store pairs of keys and values. They are incredibly useful.
"""

"""
A literal dictionary is written like this
"""

a = { '1' : 2, 2 : 3, 4 : '5' }

"""
The keys and values can have (almost) arbitrary types, but in 99.9% of all cases all keys have the same type and all values have the same type.
Very often, the keys are strings.
"""
b = {'red' : 2, 'blue' : 5, 'yellow' : 10}

"""
The value to a key in a dictionary can be obtained with square brackets
"""

print a['1']
print a[4]

"""
Dictionaries can also be created with keyword arguments
"""

c = dict(red=2, blue=5, yellow=10)

"""
A dictionary can also be thought of as a mapping between key and values, a bit similar to a function, but with explicitly given (finite) domains.
"""

double = {1 : 2, 2 : 4, 3 : 6, 4 : 8, 5 : 10}

"""
List with all keys and values can be extracted from the dictionary. These list are ordered such that corresponding keys and values are at identical positions.
"""

print b.keys()
print b.values()

"""
Dictionaries can also be created from a list of key-value tuples. Such a list can be conveniently created with the zip function
"""

#These are identical to b and c
d = dict([('red',2),('blue',5),('yellow',10)])
e = dict(zip(b.keys(),b.values()))


"""
It is simple to iterate over all keys of a dictionary. However, the order is not defined.
"""

for key in d:
    print key, d[key]

"""
Often it is necessary to iterate over both keys and values
"""

for key, value in d.items():
    print key, value

"""
Quiz
====

 - If a dictionary is a bit similar to a function, why is there no built in method for the inverse of a dictionary?
 - How can one find the number of key value pairs in a dictionary?
 - What is the return type of the items() method?

Practical Exercise
==================

A game with dice with colored faces, each color gives a different amount of points. Red gives 2 points, blue 5 points, yellow 10 points.

Write a function that for a list of colors calculates the total sum of points.
"""

def total_points(colors):
    total = 0

    #insert your code here

    return total


print total_points(["yellow","yellow","blue","red"]) == 27
