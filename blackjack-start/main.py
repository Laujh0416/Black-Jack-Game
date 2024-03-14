import random
import art
#intro = input("Do you want to play Blackjact? Type y for yes or n for no:\n")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_dict = {}
player1 = "user"
player2 = "computer"

logo = art.logo
print(logo)
def game_start():
  cards_distributor()
  result = if_over_21()
  if result == True:
    print("********************You Win!********************")
  if result == False:
    print("********************Computer Wins!********************")
    print(f"Computer's cards: {game_dict[player2]}")
    
def cards_distributor():
  cards_collection1 = []
  cards_collection2 = []
  num_cards = 2
  while num_cards > 0:
    random_cards1 = random.choice(cards)
    random_cards2 = random.choice(cards)
    cards_collection1.append(random_cards1)
    cards_collection2.append(random_cards2)
    game_dict[player1] = cards_collection1
    game_dict[player2] = cards_collection2
    num_cards -= 1
  caculation(player1)
  caculation(player2)
  #print(cal)
  #print calculation
  if_ace(player1)
  if_ace(player2)
  if player1 == "user":
    print(f"Your cards: {game_dict[player1]}")
  if player2 == "computer":
    print(f"Computer's first card is {game_dict[player2][0]}")
  return cards_collection1, cards_collection2


def caculation(player):
  sum = 0
  for value in game_dict[player]:
    sum += value
  return sum

def if_ace(player):
  value = game_dict[player]
  if value[0] == 11 and value[1] == 10:
    if player == "user":
      return True
    if player == "computer":
      return False
  elif value[1] == 11 and value[0] == 10:
    if player == "user":
      return True
    if player == "computer":
      return False

def get_other_card(player):
  another_random_card = random.choice(cards)
  game_dict[player].append(another_random_card)
  if player == "user":
    print(f"Now you have {game_dict[player]}")
  return game_dict
    
def if_over_21():
  draw = ""
  if caculation(player1) == 21:
    if if_ace(player1) == True:
      return True
      if caculation(player1)> 21:
        return False
      else:
        answer = (input("Do you want to get another card? y for yes or n for no:\n")).lower()
        if answer == "y":
          get_other_card(player1)
          caculation(player1)
          if_ace(player1)
          if_over_21()
        else:
          if caculation(player2) < 17:
            get_other_card(player2)
            caculation(player2)
            if_ace(player2)
            if_over_21()
          if caculation(player) > 21:
            #print("You Win!")
            return True
          else:
            if caculation("computer") > caculation("user"):
             # print(f"Computer's total: {caculation('computer')}")
             # print(f"Your total: {caculation('user')}")
              #print("Computer Wins ahhhhhhhh!")
              return False
            elif caculation("user") > caculation("computer"):
              #print(f"Computer's total: {caculation('computer')}")
              #print(f"Your total: {caculation('user')}")
              #print("You Win!")
              return True
            else:
              return print("Draw!")
    elif if_ace(player2) == False:
      return False
  else:
    answer = (input("Do you want to get another card? y for yes or n for no:\n")).lower()
    if answer == "y":
      get_other_card(player1)
      caculation(player1)
      if_ace(player1)
      if_over_21()
    else:
      while caculation(player2) < 17:
        #print("HERE")
        get_other_card(player2)
        caculation(player2)
        if_ace(player2)
        #if_over_21()
      if caculation(player2) > 21:
        #print("You Win!")
        return True
      else:
        if caculation("computer") > caculation("user"):
         # print(f"Computer's total: {caculation('computer')}")
         # print(f"Your total: {caculation('user')}")
          #print("Computer Wins ahhhhhhhh!")
          return False
        elif caculation("user") > caculation("computer"):
          #print(f"Computer's total: {caculation('computer')}")
          #print(f"Your total: {caculation('user')}")
          #print("You Win!")
          return True
        else:
          draw += "Draw!"
          return draw
  if draw != "Draw!":
    return False
        
start = game_start()
print(game_dict)
