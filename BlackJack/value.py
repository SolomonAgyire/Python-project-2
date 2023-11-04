
def card_value(card_rank):
  if card_rank > 13 or card_rank < 1:
    return None

  if card_rank == 11 or card_rank == 12 or card_rank == 13:
    # Jacks, Queens, and Kings are worth 10.
    return 10
  elif card_rank == 1:
    # Aces are worth 11.
    return 11
  else:
    # All other cards are worth the same as
    # their rank.
    return card_rank