def blackjack_or_bust(hand):
  if hand == 21:
    return 'BLACKJACK!'
  elif hand > 21 and hand <= 31:
    return 'BUST.'
  elif hand > 31 or hand < 4:
    return 'BAD HAND VALUE!'