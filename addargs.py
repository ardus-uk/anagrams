#!/usr/bin/python3

# this demonstrates how data can be passed into a python script
# on the command-line invocation

# usage: ./addargs.py number1 number2 number3 etc

import sys 

# we are going to add the numbers which will be in the list argv
# the first item in the list, argv[0], must be discarded as it is not a number
# (it is the name of the script)
# so we take the  list slice argv[1:]

# the numbers are interpreted as strings, so we need to convert them to numbers
# which we can do with a "map" implemented using a "list comprehension"

numbers = [float(x) for x in sys.argv[1:]]

print (numbers)
print("Sum of the numbers is",sum(numbers))