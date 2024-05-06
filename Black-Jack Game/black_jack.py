import random
logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""

print(logo)
print("WELCOME TO THE BLACKJACK GAME!!")
deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
end_game = False


def blackjack(players_sum,comp_cards):

  players_diff = abs(21 - players_sum)
  comps_diff =abs(21 - sum(comp_cards))
  if comps_diff > players_diff :
    print(f"Computer's cards : {comp_cards}")
    print("You won!")

  elif players_diff > comps_diff:
    print(f"Computer's cards : {comp_cards}")
    print("You lose!")
  elif players_diff == comps_diff:
    print(f"Computer's cards : {comp_cards}")
    print("Draw!")
  end_game = True
  start()


def cards(comp,player):
  while not end_game:
    ch1 = random.choice(deck)
    ch2 = random.choice(deck)
    comp.append(ch1)
    comp.append(ch2)
    ch3 = random.choice(deck)
    ch4 = random.choice(deck)
    player.append(ch3)
    player.append(ch4)
    print(f"One of the computer's card is : {comp[0]}")
    print(f"Your cards : {player}")
    sum_player = sum(player)
    print(f"Sum of yours cards is : {sum_player}")
    draw_card = input("Type 'y' if you want to draw another card and 'n' if you want to continue with the same cards : ").lower()
    if draw_card == "y":
      ch5 = random.choice(deck)
      player.append(ch5)
      sum_player = sum(player)

      if sum(player) > 21 and 11 in player:
        player.remove(11)
        player.append(1)
        print(f"Your cards : {player} and sum of your cards :{sum(player)}")
      elif sum(player) > 21:
        print(f"Your cards : {player} and sum of your cards :{sum(player)}")
        print(f"Computer's cards : {comp} and sum of comp's cards :{sum(comp)}")
        print("You lose!")
        start()
      else:
        print(f"Your cards : {player} and sum of your cards :{sum(player)}")
        blackjack(sum_player,comp)

    elif draw_card == "n":
      blackjack(sum_player,comp)
    else:
      print("Invalid input!")
      start()


def start():
  comp = []
  player = []
  x = input("Type 'y' to start a new game or 'n' to exit : ").lower()
  if x == "y":
    cards(comp,player)
  elif x == "n":
    global end_game
    end_game = True
    print("Thanks for playing blackjack game!")
  else:
    print("Invalid input!")


start()