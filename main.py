import random 

bestscore = 0

response = input("Would you like to play the number guessing game? y for yes, n for no...: ")

while response == "y":
  number = random.randint(1, 100)
  count = 0
  guess = input("Guess a number from 1 to 100: ")
  guess = int(guess)
  while guess > 100 or guess < 1:
    guess = input("Guess another number from 1 to 100, your number was invalid! ")
    guess = int(guess)
    
  count += 1
  
  if guess < number:
    print("The answer is higher!")
  if guess > number:
    print("The answer is lower!")
  
  while guess != number:
    print("Try again!")
    guess = input("Guess a number from 1 to 100: ")
    guess = int(guess)
    count += 1
  
    if guess < number:
      print("The answer is higher!")
    if guess > number:
      print("The answer is lower!")
  
  if guess == number:
    print("You're correct!")
    if count > 1:
      print("You got it in " + str(count) + " guesses!")
    if bestscore == 0:
      bestscore = count
    if count < bestscore:
      print("You beat the highscore of " + str(bestscore) + "! Congratulations!")
      bestscore = count
    if bestscore < count:
      print("The best score is " + str(bestscore) + " guesses")
  if count == 1:
    bestscore = 1
    response = "n"
  if response != "n":
    response = input("Do you want to retry? y for yes, n for no: ")
if bestscore == 1:
  print("You beat the game! You got the near impossible score of 1!")
  print("Great job!")
if response != "y":
  print("We hope to see you again!")
