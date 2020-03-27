import random
#Game score of two players
game_score1 = 0
game_score2 = 0
round_score = 0

print('-------------------')
print('Turn of Player 1')   
print('-------------------')
print('Your game score is ' + str(game_score1) )
print('-------------------')
player = 1
while game_score1 < 50 and game_score2 < 50:
    roll = random.randint(1, 6)
    if roll != 1:
      print('You rolled a ' + str(roll))
      round_score = round_score + roll
      roll_again = input('Your round score is ' + str(round_score) + '.' + ' Roll again (y/n)') 
      if roll_again == 'n':
        if player == 1:
          #Update the game score of player 1
          game_score1 = round_score + game_score1
          if game_score1 < 50:
            player = 2
            round_score = 0
            print('')
            print('Turn of Player 2')
            print('-------------------')
            print('Your game score is ' + str(game_score2))
            print('-------------------')
          else:
            print('-------------------')
            print('Player 1 WON!!!!!')
        elif player == 2:
          #Update the score for player 2
          game_score2 = round_score + game_score2
          if game_score2 < 50:
            player = 1
            round_score = 0
            print('')
            print(' Turn of player 1')
            print('-------------------')
            print('Your game score is ' + str(game_score1))
            print('-------------------')
          else:
            print('-------------------')
            print('Player 2 WON!!!!!')   
    elif roll == 1:
      round_score = 0
      print('You rolled a ' + str(roll))
      if player == 1:
        player = 2
        print('')
        print('Turn of Player 2')
        print('-------------------')
        print('Your game score is ' + str(game_score2))
        print('-------------------')
      elif player == 2:
        player = 1
        print('')
        print('Turn of Player 1')
        print('-------------------')
        print('Your game score is ' + str(game_score1))
        print('-------------------')




    
 