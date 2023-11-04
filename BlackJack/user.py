from random import randint
from end_status import blackjack_or_bust
from value import card_value
from name import draw

def play_human_turn():
  starting_value = 0
  hand_value = 0
  while starting_value <2:
    card_choice = randint(1,13)
    print(draw(card_choice))
    hand_value += card_value(card_choice)
    starting_value+=1

  while hand_value <21 :
    valid = input(f'You have {hand_value}. Hit (y/n)? ')
    if valid.strip().lower() == 'y':
      next_card_choice = randint(1,13)
      print(draw(next_card_choice))
      hand_value += card_value(next_card_choice)
    elif valid.strip().lower() == 'n':
      break
    else:
      print("Sorry I didn't get that.") 

  print(f'Final hand: {hand_value}.')
  if blackjack_or_bust(hand_value):
      print(blackjack_or_bust(hand_value))