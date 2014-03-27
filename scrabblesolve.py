#!/usr/bin/env python

#scrabble solver
import sys
from itertools import permutations
from string import join

wordlist_path = "/usr/share/dict/words"
MAX_LENGTH = 8 #max pieces in scrabble

point_dict = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r':
1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10} 

def create_wordlist():
    word_list = [] #host words 7 or less characters
    with open(wordlist_path) as wordlist:
	for line in wordlist:
	    line = line.rstrip('\n')
	    if len(line) > MAX_LENGTH:
		continue
	    word_list.append(line)
    return word_list

def word_arrange(user_letters): #function to arrange the letters in to all combinations
    letters_permu = []
    arranged_words = []

    for num in range(len(user_letters)+1): #plus 1 since lists are index-0.
	if not (num == 0 or num == 1): #ignore 0 and 1 letter words
	    letters_permu.extend(list(permutations(user_letters, num)))

    for item in letters_permu:
	arranged_word = "".join(item)
	arranged_words.append(arranged_word)	

    return arranged_words


def filter_words(arranged_words, word_list):
    approved_words = set(arranged_words).intersection(word_list)
    return approved_words

def score_calc(approved_words):

    score_list = [] 
    for word in approved_words:
	scoresum = 0
	for letter in word:
	    scoresum += point_dict[letter]
	score_list.append((scoresum, word))
    score_list = sorted(score_list, reverse=True)
    return score_list


word_list = create_wordlist()
arranged_letters = word_arrange(sys.argv[1])
approved_words = filter_words(arranged_letters, word_list)
score_list = score_calc(approved_words)

for item in score_list[0:10]:
    print item[0], item[1] 
