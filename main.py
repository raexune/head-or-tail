#Write your code below this line 👇
#Hint: Remember to import the random module first.🎲

import random


while True:
  guess = input("Head or tail? ").strip().capitalize()
  outcome = random.randint(0,1)

  if outcome == 1:
      outcome = "Head"
  elif outcome == 0:
      outcome = "Tail"
    
  if guess == outcome:
    print("You won.")
  else:
    print("You lose.")






