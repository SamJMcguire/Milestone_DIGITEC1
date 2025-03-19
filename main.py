'''This is a place holder'''
'''
Rumplestilkson 


'''

# Import library or external code. OS for sleep and clear screen
import os

# Set variables for list, user guess, guess counter 

INT_GUESSREMAINING = 3
bool_endLoop = False
str_userGuess = ''
str_userName = ''

# Creating game functions

def greeting():
    str_userName = input("Hello.  What is your name?")
    print(f"Hello {str_userName}")
    
    
# The Main program
greeting()
