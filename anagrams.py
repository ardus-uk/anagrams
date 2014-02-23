#!/usr/bin/python3
with open('./wordsEn.txt') as f:
	lines = f.readlines()  # lines is a list of words
	word = 'leas'
	letters = list(word)
	n = len(letters)
	cands = [elem for elem in lines if (len(elem)==n+1)]
	i=0
	for letter in letters:
		num = letters.count(letter)
		cands = [elem for elem in cands if (letter in elem) and elem.count(letter) == num]
	for cand in cands:
		print (cand)
