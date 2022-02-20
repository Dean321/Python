# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 17:09:39 2021

@author: Dean321

Popular Rock/Paper/Scissors game
Rules are 
    Scissors cut Paper
    Paper covers Rock
    Rock crushes Scissors    
    
Have fun playing with the computer
"""

import random
r = random.randint(0,2)
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]
choice = int(input("Enter your choice 0 - Rock, 1 - Paper, 2 - Scissor : "))
print("Your Choice: \n"+options[choice]+"\nComputer Choice: \n"+options[r])
if options[r]==options[choice]:
    print("It's a draw!!!")
else:
    if((options[r] == options[0] and options[choice]!=options[1]) or (options[r] == options[1] and options[choice]!=options[2]) or (options[r] == options[2] and options[choice]!=options[0])):
        print("Computer Wins")
    else:
        print("Player wins")