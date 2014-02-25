#!/usr/bin/python3

# this demonstrates some list operations, including maps and filters using list comprehensions

numberlist = [1,1,2,3,3,3,3,4,5,6,6,6,6,6,6,6,7]
wordlist =['oh','to','be','in','England','now','that','Spring','is','here']

print(numberlist)
print(wordlist)
print('--------------------------------------------')

# a slice
alist = wordlist[3:5]
print (alist)
print('--------------------------------------------')

# a bigger slice
blist = wordlist[:5]
print(blist)
print('--------------------------------------------')

# a copy of a list
clist = wordlist[:]
print(clist)
print('--------------------------------------------')

# the number of items in a list
print (len(wordlist))
print('--------------------------------------------')

# the number of occurrences of an item in a list
print (numberlist.count(6))
print('--------------------------------------------')

# the index of the first occurrence of an item in a list
print (numberlist.index(3))
print('--------------------------------------------')

# reverse the list order
wordlist.reverse()
print(wordlist)
print('--------------------------------------------')

# and reverse it back
wordlist.reverse()
print(wordlist)
print('--------------------------------------------')

# a map, using list comprehension
dlist = [2*x for x in numberlist]
print(numberlist)
print(dlist)
print('--------------------------------------------')

# a filter, using list comprehension
elist = [x for x in numberlist if x > 3]
print(numberlist)
print(elist)
print('--------------------------------------------')

# another filter, using list comprehension
flist = [x for x in wordlist if len(x) > 2]
print(wordlist)
print(flist)
print('--------------------------------------------')

# another filter, using list comprehension
glist = [x for x in wordlist if 'a' in x]
print(wordlist)
print(glist)
print('--------------------------------------------')