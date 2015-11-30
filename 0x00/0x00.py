"""
0x00

Lists and tuples
================

Both lists and tuples can contain a number of elements that don't need to be of the same type. The big difference is that lists are mutable, i.e. can be changed after creation, while tuples are immutable. That makes them suitable choices for different situations.
"""

#tuple with three elements
t1 = (1,2,"b")
#tuple with one element
t2 = (1,)

#list with three elements
l1 = [1,2,5]
#list with one element
l2 = [1]

"""
As a rule of thumb, tuples are used if the number of the elements is relatively small and their types are different, but fixed and known.
Use lists to hold a unknown number of elements of the same type.

The variable names of lists often end with a s to emphasize the plurality of elements.
"""

customer = ("John", "Doe", 32, "Birmingham")
places = ["Moscow", "London", "Canberra", "Buenos Aires"]

"""
tuples can be unpacked to individual variables by a very concise syntax. Lists can not.
"""

a,b,c = t1

"""
both lists and tuples can be used in a for loop, but if you want to use it in a for loop, you should use a list
"""

#usually not desireable
for c in customer:
    print c

for place in places:
    print place

"""
both lists and tuples can be indexed with square brackets
"""

print customer[1]
print places[2]

"""
one can convert between the two
"""

tuple(l1)
list(t2)

"""
Quiz
====
    - Why is the syntax for a one element tuple the way it is?
    - What would you use for:
      - The x and y coordinates of a point in 3D space?
      - The prime numbers smaller than 83?
      - The return type of a function that returns the coordinates of all possible places a chess piece can move to in a specific situation?
    - What is the return type of the enumerate function?


Practical exercise
==================

Write two functions that print the first n elements of the Fibonacci sequence. For the first use a for loop to populate a list. For the second use a recursive function.

"""

def fibolist(n):
    res = []

    #fill your code here

    print res

def fiborec(n, prev = (0,1)):
    print prev[1]

    #fill your code here



#uncomment during development to test
#fibolist(10)
#fiborec(10)
