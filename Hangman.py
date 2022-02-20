# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 11:50:30 2021

@author: Dean321

The popular Hangman game. The game is a paper and pencil guessing game for two or more players. 
One player thinks of a word and the others try to guess it by suggesting 
letters within a certain number of guesses, here it is 7.
Enjoy playing this. Have fun.
"""


word_list = ["appearance", "birthday", "chocolate", "enforcement"]


import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

r = random.randint(0,len(word_list)-1)
chosen_word = word_list[1]
turns = 5
ans = ""
chars = []
for w in chosen_word:
    ans+="_ "
    chars.append("_ ")

while turns > -1 and ans!=chosen_word:
    print(ans)
    print(f"You have {turns+1} turns remaining")
    a = input("Guess a alphabet and type your answer in lower-case ").lower()
    if a in chosen_word:
      
      for w in range(0, len(chosen_word)):
          
          if a == chosen_word[w]:
              chars[w]=a
      ans=""
      for c in chars:
          ans+=c
    else:
      print(stages[turns])
      turns-=1
      print("Try Again!")

if ans==chosen_word:
    print("You Win")
else:
    print("You Lost. Try Again")