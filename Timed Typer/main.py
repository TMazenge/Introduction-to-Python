import dictionary
import timer

def get_num_words_by_level(level):
  """Returns the number of words to type for the given level.
  """
  if level == 1 or level == 2 or level == 3 or level == 6:
    num_words = 1
  elif level == 4:
    num_words = 2
  elif level == 5:
    num_words = 3 
  return num_words  

def get_timeout_by_level(level):
  """Returns the time limit, in seconds, for the given level."""
  if level == 1:
    time_out = 10
  elif level == 2:
    time_out = 8
  elif level == 3 or level == 4 or level == 5:
    time_out = 6
  elif level == 6:
    time_out = 3
  return time_out

def get_phrase(level):
  """Returns a phrase to type based on the level."""
  # Get the number of words that are supposed to be in
  # the phrase to type, according to the level.
  num_words_in_phrase = get_num_words_by_level(level)
  phrase = ''
  while num_words_in_phrase > 0:
    # Continue adding words to the phrase until it has
    # the appropriate number of words.
    word = dictionary.get_random_word(1)
    phrase = phrase + ' ' + word
    num_words_in_phrase = num_words_in_phrase - 1
  return phrase.strip()
 
level = 1
rounds = 0
type_in = 0

#Ends the game if times runs out
while type_in != '':
  phrase = get_phrase(level)
  word = ' TYPE: ' + phrase
  print(word)
  print(' YOU HAVE ' + str(get_timeout_by_level(level)) + ' SECONDS......')
  
  #Aks an input from the user with a time limit
  type_in = timer.input_with_timeout(get_timeout_by_level(level))
  print(' ----------------')
  rounds += 1
  #Ends the game if word is misspelled
  if type_in != phrase and not type_in == '':
    print(' Incorrect spelling!!')
    break
  if level < 6: # increase level until level 6
    #New level is unlocked if 5 rounds are reached in that level 
    if rounds % 5 == 0:
      level += 1
      print(' START NEXT LEVEL ' + '(' + str(level) + ')')
      print(' ----------------')
print(' GAME OVER')
print(' You took ' + str(rounds) + ' rounds.')
