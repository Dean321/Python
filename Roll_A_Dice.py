# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 16:27:08 2022

@author: Dean321
"""
import random
dice=[
"""
-----
|   |
| o |
|   |
-----
""" ,
'''
-----
|o  |
|   |
|  o|
-----
''',
'''
-----
|o  |
| o |
|  o|
-----
'''  ,
'''
-----
|o o|
|   |
|o o|
-----
''',
'''
-----
|o o|
| o |
|o o|
-----
''',
'''
-----
|o o|
|o o|
|o o|
-----
'''
]

choice = "y"
while(choice == "y"):
    choice = input("enter 'y' to roll dice or 'n' to stop")
    if choice == "y":
        r = random.randint(0,5)
        print(dice[r],sep="\n")
    
                   