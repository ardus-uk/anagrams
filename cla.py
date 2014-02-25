#!/usr/bin/python3

# this demonstrates how data can be passed into a python script
# on the command-line invocation

# usage: ./cla.py arg1 arg2 'arg3 contains some spaces' arg4 etc

import sys #this is the module giving access to some useful functions

# sys.argv is the list of items on the command line
# each item is a string object
# the first item, argv[0], is the name of the script

print(sys.argv) 