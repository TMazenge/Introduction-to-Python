# Tell the user to pick an animal.
print('Think of one of the following:')
print('goat, owl, lion, penguin, crab, bat, octopus, monkey')
print('----------------------------')

# Ask the user a series of yes or no questions to guess their animal.
question = input('Does it have 4 legs (y/n)? ')
if question  == 'y':
  question1 = input('Does it live on a farm (y/n)? ')
  if question1 == 'y':
    print('It must be a goat!')
  else:
    print('It must be a lion!')
elif question == 'n': 
  question2 = input('Can it fly (y/n)? ')
  if question2 == 'y':
    question3 = input('Is it blind (y/n)? ')
    if question3 == 'y':
      print('It must be a bat!')
    else:
      print('It must be an owl!')
  if question2 == 'n':
    question4 = input('Is it aquatic (y/n)? ')
    if question4 == 'y':
      question5 = input('Can it walk on two legs (y/n)? ')
      if question5 == 'y':
        print('It must be a penguin!')
      elif question5 == 'n':
        question6 = input('Can it walk on sand (y/n)? ')
        if question6 == 'y':
          print('It must be a crab!')
        else:
          print('It must be an octopus!')
    if question4 == 'n':
      print('It must be a monkey!')