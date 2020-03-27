import random

easy_words = [
  'bat',
  'dog',
  'toy',
  'cat',
  'rat',
  'law',
  'mud',
  'boy',
  'the',
  'she',
  'red',
  'pop',
  'lie',
  'bay',
  'hay',
  'can',
  'sad',
  'mad',
  'cap',
  'rap',
  'met',
  'fad',
  'hop',
  'top',
  'tap',
  'lap',
  'lie',
  'bag',
  'ham',
  'ray',
  'say',
  'tie',
  'bit',
  'hit',
  'hat',
  'bet',
  'bid',
  'lid',
  'pad',
  'and',
  'tan',
  'tar',
  'eat',
  'ate',
  'lag',
  'rag',
  'tag',
  'kid',
  'dip',
  'rip',
  'lip',
  'pod',
  'rod',
  'nod',
  'his',
  'sis',
  'gem',
  'ant',
  'wad',
  'win',
  'nap',
  'way',
  'pay',
  'day',
  'van',
  'mom',
  'dad',
  'dot',
  'rot',
  'tip',
  'hen',
  'tin',
  'fee',
  'pee',
  'tee',
  'tea',
  'pea',
  'bee',
  'sea',
  'see',
  'men',
  'man',
  'did',
  'sim',
  'pin',
  'fib',
  'yay',
  'may',
  'gay',
  'pot',
  'pan',
  'run',
  'ran',
  'ton',
  'put',
  'hut',
  'but',
  'cut',
  'pit',
  'vat',
]

hard_words = [
  'congratulations',
  'absolutely',
  'photosynthesis',
  'monstrosity',
  'university',
  'cheeseburger',
  'accommodate',
  'suburban',
  'pizazz',
  'assuming',
  'stewardess',
  'xylophone',
  'overzealous',
  'withdrawal',
  'wednesday',
  'vulnerable',
  'visualization',
  'versatile',
  'veterinary',
  'vaccination',
  'vegetarian',
  'unanimous',
  'transmission',
  'trajectory',
  'temporary',
  'tournament',
  'temperature',
  'surveillance',
  'psychology',
  'responsibility',
  'recommendation',
  'pronunciation',
  'practicioner',
  'plagiarism',
  'pilgrimage',
  'philosophy',
  'participation',
  'nutritious',
  'necessarily',
  'miscellaneous',
  'marshmallows',
  'mayonnaise',
  'leprechaun',
  'limousine',
  'kindergarten',
  'knowledgeable',
  'interference',
  'inflammation',
  'handkerchief',
  'fluorescent',
  'extraordinary',
  'pharmaceutical',
  'exhiliration',
  'environmental',
  'disappointment',
  'choreography',
  'circumstantial',
  'cauliflower',
  'cantaloupe',
  'auditorium',
  'apostrophe',
  'amphitheater',
  'advantageous',
  'acknowledgement',
  'abbreviation',
  'abundant',
  'accommodation',
  'adjustment',
  'ambidextrous',
  'asymmetrical',
  'auxiliary',
  'bachelorette',
  'bureaucracy',
  'behavioral',
  'boulevard',
  'camouflage',
  'determination',
  'differentiation',
  'description',
  'dysfunctional',
  'impressionable',
  'enthusiastic',
  'entrepreneur',
  'eavesdropping',
  'exaggerated',
  'fascinating',
  'governmental',
  'hygienic',
  'immediately',
  'individuality',
  'interpretation',
  'laboratory',
  'labyrinth',
  'lieutenant',
  'lightning',
  'legitimate',
  'likelihood',
  'maintenance',
  'masquerade',
  'medicinal',
  'mezzanine',
  'medieval',
  'mischievous',
  'misunderstood',
  'pneumonia',
  'noticeable',
  'opportunity',
  'overwhelming',
  'picturesque',
  'pilgrimage',
  'prohibitive',
  'quadruple',
  'ridiculous',
  'sacrilegious',
  'rudimentary',
  'chandelier',
  'sophomore',
  'superfluous',
  'susceptible',
  'suspicious',
  'synonymous',
  'tomorrow',
  'zucchini',
]

def get_random_word(difficulty):
  """Returns a random word from the dictionary.
  
  Args:
    difficulty: 1 or 2, where 1 is an easy word and 2 is a hard word.

  Returns:
    A random word of the specified difficulty.
  """
  if difficulty == 1:
    words = easy_words
  else:
    words = hard_words

  return random.choice(words)