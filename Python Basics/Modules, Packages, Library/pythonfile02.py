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