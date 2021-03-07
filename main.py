import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  return random.choice(cards)

def calculate_score(cardlist):
  Sum = sum(cardlist)
  if len(cardlist) == 2 and 11 in cardlist and 10 in cardlist:
    return 0
  elif 11 in cardlist and Sum > 21:
    cardlist.remove(11)
    cardlist.append(1)
  else:
    return Sum

def compare(user_score, computer_score):
  if computer_score == user_score:
    return "Draw"
  elif computer_score == 0:
    return "You Lose"
  elif user_score == 0:
    return "You Win"
  elif user_score > 21:
    return "You Lose"
  elif computer_score > 21:
    return "You Win"
  elif user_score > computer_score:
    return "You Win"
  else:
    return "You Lose"


def play_game():
  user_cards = []
  computer_cards = []
  is_game_over = False

  while len(user_cards) < 2:
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      draws =input("Do you want to draw another card? Y/N: ")
      if draws == "Y" or draws == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()