#!/usr/bin/python3

# defines a function, unique, 
# which examines each element of a list
# and, if it has not been previously encountered,
# adds it to a new list.
# This ensures that the new list contains all the elements of the first list, 
# but with no duplicates

def unique(listx):
	listy=[]
	for x in listx:
		if x not in listy:
			listy.append(x)
	return listy

# for example
firstlist = [1,2,3,4,4,2,5,6,3,2,6,7,8,11,15]
print (firstlist)
print (unique(firstlist))
