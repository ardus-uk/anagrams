#!/usr/bin/python3
import sys

if len(sys.argv)!=2:
	print ("Usage: ./anagram3.py <word>")
	sys.exit()

word = sys.argv[1]

def unique(listx):
	listy=[]
	for x in listx:
		if x not in listy:
			listy.append(x)
	return listy

with open('./wordsEn.txt') as f:
	lines = f.readlines()  # lines is a list of words
	#word = 'refined'
	letters = list(word)  # letters is a list of the letters
	unique_letters = unique(letters)
	n = len(letters)
	cands = [elem for elem in lines if (len(elem)==n+1)]
	i=0
	for letter in unique_letters:
		num = letters.count(letter)
		cands = [elem for elem in cands if (letter in elem) and elem.count(letter) == num]
	for cand in cands:
		print (cand.strip())
