"""
0x04

A Birthday remainder
====================

Now it is time to put everything together. The goal is to write a script that reads the birthday dates from a file and prints out the next five upcoming birthdays.
"""

"""
For this we need to work with dates. Luckily python has all the functionality already included in the datetime package
"""

import datetime

"""
A date object represents a specific day
"""

yesterday = datetime.date(2015,12,4)

"""
The current date can be obtained like this
"""

today = datetime.date.today()
print today

"""
Subtracting two dates yields a timedelta object, which can be asked for the number of days between the two dates.
"""

delta = today - yesterday
print delta.days


"""

Practical Exercise
==================

Write a script called birthday.py that reads a file called birthday.dat for a list of birthdays. It then finds the next 5 birthdays and prints them with the number of days remaining until. Take care to correctly handle the year change.
"""
