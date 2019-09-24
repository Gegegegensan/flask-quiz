# -*- coding: utf-8 -*-

from random import shuffle
print ('Welcome to Eiken Vocab Quiz')

with open("Eiken-2.txt") as f:
	lines = f.readlines()

shuffle(lines)
numRight = 0
wrong = [ ]

numQuestions = int(input("How many questions would you like to take?  "))

for line in lines[:numQuestions]:
	question, rightAnswer = line.strip().split("\t")
	answer = raw_input('What is ' + question + ' in English?' + ' => ')
	if answer.lower() == rightAnswer:
		print('You got a right Answer. \n')
		numRight += 1

	else:
		print('No, the answer is %s.' % rightAnswer + "\n")
		wrong.append(question)

print('You got %d right' % (numRight)) + "\n"
if (wrong):
	print ('You got these wrong: ')
	for q in wrong:
		print (q)