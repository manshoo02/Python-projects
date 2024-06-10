import random
logo ="""
   _____                       _   _                                  _
  / ____|                     | | | |                                | |
 | |  __ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|


"""
print(logo)
print("WELCOME TO THE NUMBER GUESSING GAME!")
print("I'M THINKING OF A NUMBER BETWEEN 1 AND 100. Guess the number")
num = random.randint(1,100)


def guess_the_num(number):
  game_over = False
  diff = input("CHOOSE THE DIFFICULTY,. Type 'easy' or 'hard. ").lower()
  if diff == "easy":
    no_of_guess = 10
  elif diff == "hard":
    no_of_guess = 5
  else:
    ("INVALID INPUT!")
  print(f"You have {no_of_guess} guesses remaining to guess the number.")

  while not game_over and no_of_guess >0:
    guess = int(input("Make a guess :"))
    no_of_guess -=1
    if guess > number:
      print("Too high")
    elif guess < number:
      print("Too low")
    else:
      print("You got it right.")
      game_over = True

  if not game_over:
    print(f"You failed to guess the number , the answer was {number} ")
  start()

def start():
  x = input("DO YOU WANT TO START A NEW GAME? Type 'yes' or 'no'.").lower()
  if x == 'yes':
    guess_the_num(num)
  elif x == 'no':
    print("Thanks for playing the game!")
  else:
    print("INVALID INPUT!")
    x = input("DO YOU WANT TO START A NEW GAME? Type 'yes' or 'no'.").lower()
    if x == "yes":
        guess_the_num(num)
    elif x == "no":
      print("Thanks for playing the game!")
    else:
      print("INVALID INPUT!")
      start()

start()