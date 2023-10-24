#!/usr/bin/env python

import random 

def main():
     """Start a music guessing game ."""    
     print ("guess the music")

     max_trials = 5
trials = 0 
score = 50 #initialize the score 50 
 

music_genres = [
    "justin timberlake",
    "sia",
    "lady gaga",
    "txt",
    "enha",
    "newjeans"
     ]
 
x = (random.choice("kpop and hip hop"))
guess = None 

while x != guess:

    guess = str(input("what artist am i thinking of ?"))
    trials +=5
                 
    if x == guess:
        prin("you guessed {}. fulamak betul do".format(guess))
        score += 20
   
    else:
      print("you guessed {}. weh salah la,buat balik!".format(guess))
      score -= 10
      print(score)


main()