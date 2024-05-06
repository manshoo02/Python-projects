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
print("Welcome to the Rock Paper Scissors Game!")
import random
series = int(input("Enter the number of times you want to play : "))
win = 0
comp_win = 0
draw = 0
valid_games = 0
for i in range(1,series +1):
    choice = int(input("Type 0 for 'rock' , 1 for 'paper' and 2 for 'scissors'"))
    comp = random.randint(0,2)
    game = [rock,paper,scissors]

    if choice not in [0,1,2]:
        print("Invalid choice")
        continue
    valid_games += 1
    print(f"Computer chose: {game[comp]}")
    print(f"You chose: {game[choice]}")

    if comp == choice:
        draw += 1
        print("Draw!")
    elif (comp == 0 and choice == 1) or (comp == 1 and choice == 2) or (comp == 2 and choice == 0):
        win += 1
        print("You won!")
    else:
        comp_win += 1
        print("Computer won")


    
print(f"You won {win} times out of {valid_games} times.")
print(f"Computer won {comp_win} times out of {valid_games} times.")
print(f"It was a draw - {draw} times out of {valid_games} times.")

    
