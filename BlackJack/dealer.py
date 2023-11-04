from random import randint
from end_status import blackjack_or_bust
from value import card_value
from name import draw

def play_dealer_turn():
  hand_value = 0
  starting_value = 0
  while starting_value <2:
    card_choice = randint(1,13)
    print(draw(card_choice))
    hand_value += card_value(card_choice)
    starting_value +=1
  
  if (hand_value) < 17:
    print(f'Dealer has {hand_value}.')

  while hand_value<17:
    draw_another_card = randint(1,13)
    hand_value += card_value(draw_another_card)
    print(draw(draw_another_card))
    if hand_value <17:
      print(f'Dealer has {hand_value}.')
    
  if hand_value >= 17:
    print (f'Final hand: {hand_value}.')
    if blackjack_or_bust(hand_value):
      print(blackjack_or_bust(hand_value))