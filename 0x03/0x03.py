"""
0x03

Files
=====

Python can be used to read and write files.
"""

"""
A file is opened with the open function. This function is always available
"""
fid = open("0x03.py")

"""
After use, files must be closed with the close method.
"""
fid.close()

"""
Files can be opened in different modes, for reading, writing or both, in text mode or binary mode. By default files are opened in text read only mode. Binary mode is rarely used.

To open a file for writing, an additional parameter is supplied to the open function.
"""

fid = open("test.tmp","w")
fid.close()

"""
To read individual characters from the file, the read() method can be used. The file object maintains an internal cursor, which is advanced when reading
"""

fid = open("0x03.py")
#read first 4 characters
print fid.read(14)

#read the rest of the file
print len(fid.read())
fid.close()

"""
In most cases it is more convenient to read a file line by line
"""

fid = open("0x03.py")

#read first line
print fid.readline()
#read second line
print fid.readline()
fid.close()

"""
For this reason a file object can be used in a for loop, which then iterates over all lines of the file.
"""
fid = open("0x03.py")
for i,line in enumerate(fid):
    print i,line
    if i > 3:
        break

"""
To write, the write functions is called with the string that should be written to the file. End of lines have to be indicated by \n"
"""

fid = open("test.tmp","w")
fid.write("green\nyellow\n")
fid.write("blue\n")
fid.write("green\n")
fid.close()


"""
Quiz
====

How 


Practical Exercises
===================

Write a function that writes the first 15 Fibonacci numbers to a file with a given file name.

Write a function that reads a file and writes its contents to a file utput.txt but with the first letter capitalized.

"""

def output_fibo(filename):
    #replace with your code
    pass

def capitalize_contents(inname, outname):
    #replace with your code
    pass


#uncomment to test
#output_fibo("fibonacci.dat")
#capitalize_contents("test.tmp","test.dat")
