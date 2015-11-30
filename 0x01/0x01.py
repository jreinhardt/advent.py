"""
0x01

Strings
=======

Strings are the way to represent text. Python contains a lot of useful functionality for working with text, and is a great tool for processing text.
"""


"""
A literal string can be written in three different ways
"""

a = "Hello World"
b = 'Hello world'
c = """Hello World"""

"""
Strings can be easily split into parts
"""

print a.split()

"""
By default they are split at whitespace, but other separators can be specified
"""

print a.split("o")

"""
Sequences of strings can also be put together again
"""

print ",".join(a.split())

"""
The case of a string can be manipulated
"""

print a.upper()
print a.lower()
print b.title()

"""
A string is a sequence, and can in many situations be used very much like a list.
"""

for char in c:
    print char

print c[3]

print "W" in c


text = """
Quiz
====

    - What is the matter with all this explanatory text between the code? Why is it not printed? Why doesn't it give syntax errors?
    - Why are there different ways to write literal strings?
    - How do you determine the number of characters in a string?
    - How do you convert a string to a list of individual characters?
    - What does the strip() method do for a string? (Hint: Look up the documentation and read around a bit, there are many interesting and useful methods)

Practical exercise
==================

Write a function that returns the number of occurences of the word 'the' in a given text.

Write a function that returns a reformatted version of a given text so that there are exactly five words per line.
"""

def countthes(text):
    #replace with your code
    pass

def reformat(text):
    #replace with your code
    pass


#uncomment for testing
#countthes(text)
#reformat(text)

