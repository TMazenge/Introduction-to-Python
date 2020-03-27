"""
Simulates a simplified game of blackjack with two players:
the user and the dealer. The dealer is an automated
computer player who plays a fixed strategy in accordance
with the typical house rules.

The simplified rules do not allow for betting or splitting
pairs. The ace is always used as an 11, and cannot be
treated as a 1.
"""

import deck

play = 'yes'

while play == 'yes':
  bet = int(input('How much money do you want to bet?: '))
  name = 'PLAYER'
  hand = ''
  
  # The player draws cards
  hand = deck.draw_starting_hand(name, hand)
  if hand == 21:
    deck.print_end_turn_status(hand)
    user_hand = hand
    name = 'DEALER'
  else:
    #The player chooses to hit or stand
    while hand < 21:
      hit = input('Hit (y/n)?')
      if hit == 'y':
        pick_card = deck.draw_card(name, hand)
        hand = hand + pick_card
        if hand >= 21:
          deck.print_end_turn_status(hand)
          user_hand = hand
          name = 'DEALER'
      else:
        deck.print_end_turn_status(hand)
        user_hand = hand
        name = 'DEALER'
        break
  #The dealer draw his/her cards
  hand = deck.draw_starting_hand(name, hand)
  if hand >= 17:
    deck.print_end_turn_status(hand)
    dealer_hand = hand
  else:
    while hand < 17:
      pick_card = deck.draw_card(name, hand)
      hand = hand + pick_card
      dealer_hand = hand
      if hand >= 17:
        deck.print_end_turn_status(hand)
        dealer_hand = hand
  #The winner between dealer and player is decided
  deck.print_end_game_status(user_hand, dealer_hand, bet)    
  print('==================================')
  play = input('Do you want to play again (yes/no)? ')
  print('==================================')


