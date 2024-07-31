# Import method 01
import pythonfile01
print(pythonfile01.sum01(2,3))

# Import method 02
from pythonfile01 import sum01
print(sum01(3,9))

# Calendar module
import calendar as cl
# to print the default satart day of a week. 0 = Monday
print(cl.firstweekday())
# To check if the year is a leap year.
print(cl.isleap(2024))
# To check what day is the given date.
print(cl.weekday(2024,7,31))
# To print the entire month design of specified month of a year.
print(cl.month(2024,7))
# To print the whole calender.
print(cl.calendar(2024))

# moth Module
import math as m
print(m.ceil(3.9))
print(m.floor(3.9))
print(m.factorial(4))
print(m.exp(1))

import re
line = "Python is a programming language."
# to check if the string starts with given characters.
print(re.match("Python",line))
print(re.match("is",line)) #None
# to search if the given pattern is in the string
print(re.search("is",line))
a = re.search(("programming language"),line)
if a:
    print("Match found.")
else:
    print("No Match.")

# substitution method
newline = re.sub("programming","high",line)
print(newline)
line1 = "python is simple. python is powerful python is great"
newline1 = re.sub("python","C",line1,count=2)
print(newline1)
line2 = "4253243432 5324 python is 3423324 programming language python is a high level language"

# All numerical characters are replaced.
new1line2 = re.sub("\d","X",line2)
print(new1line2)
# All characters except numerical characters are replaced.
new2line2 = re.sub("\D","X",line2)
print(new2line2)
# All spaces are replaced.
new3line2 = re.sub("\s","X",line2)
print(new3line2)
# All characters except spaces are replaced.
new4line2 = re.sub("\S","X",line2)
print(new4line2)