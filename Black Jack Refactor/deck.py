import random

def print_card(card_rank):
  """Prints the given card's official name.
  
  Args:
    card_rank: The numeric representation of a card.
  """
  if card_rank == 1:
    card_name = 'Ace'
  elif card_rank == 11:
    card_name = 'Jack'
  elif card_rank == 12:
    card_name = 'Queen'
  elif card_rank == 13:
    card_name = 'King'
  else:
    # All other cards are named by their rank.
    card_name = card_rank

  print('Drew a ' + str(card_name))

def draw_card(name, hand):
  """Draws a new random card, prints its name, and returns its face value.

  Returns:
    The face value of the chosen card. The face
    value of a card is the same as its numeric value,
    except for the ace, jack, queen, and king.
  """
  card_rank = random.randint(1, 13)
  print_card(card_rank)
  
  if card_rank == 11 or card_rank == 12 or card_rank == 13:
    # Jacks, Queens, and Kings are worth 10.
    card_value = 10
  elif card_rank == 1:
    # Aces are worth 11.
    if name == 'PLAYER':
      card_value = int(input('What is your Ace value (1/11)?'))
    elif name == 'DEALER':
      if hand <= 10:
        card_value = 11
      else:
        card_value = 1
  else:
    # All other cards are worth the same as
    # their rank.
    card_value = card_rank
  return card_value

def print_header(message):
  """Prints the given message formatted as a header.
  
  Args:
    message: The message to be printed.
  """
  print('-----------')
  print(message)
  print('-----------')

def draw_starting_hand(name, hand):
  """Prints the turn header and draws a starting hand, which is two cards.
  
  Args:
    name: The name of the player whose turn it is.

  Returns:
    The hand total, which is the sum of the two newly drawn cards.
  """
  print_header(name + ' TURN')
  return draw_card(name, hand) + draw_card(name, hand)

def print_end_turn_status(hand):
  """Prints the hand total and status at the end of a player's turn.

  Args:
    hand: The sum of of all the cards in the hand.
  """
  print('Final hand: ' + str(hand))

  if hand == 21:
    print('BLACKJACK!')
  elif hand > 21:
    print('BUST.')

def print_end_game_status(user_hand, dealer_hand, bet):
  """Prints the end game banner and the winner based on the final hands.

  Args:
    user_hand: The sum of all the cards in the user's hand.
    dealer_hand: The sum of all the cards in the dealer's hand.
  """
  print_header('GAME RESULT')

  if user_hand <= 21 and (user_hand > dealer_hand or dealer_hand > 21):
    print('You win!')
    print('Your Payout is $' + str(bet * 2))
  elif dealer_hand <= 21 and (dealer_hand > user_hand or user_hand > 21):
    print('Dealer wins!')
    print('Sorry! You lost your bet.')
    print('Your Payout is $' + str(bet * 0))
  else:
    print('Tie.')
    print('Your Payout is $' + str(bet))
    
