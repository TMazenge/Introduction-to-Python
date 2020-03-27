def replace_with_index(string, character):
  """Replaces all instances of the character in the string with their index."""
  result = ''
  index = 0
  for letter in string:
    if letter == character:
      letter = index
      result = result + str(letter) 
    else:
       result = result + letter
    index += 1   
  return result

def text_wrap(sentence, width):
  """Prints the sentence formatted into lines with width characters each."""
  num = width
  count = 0
  index = 0
  while count < len(sentence):
    slice_word = sentence[index:num]
    print(slice_word)
    index = num
    num = num + width
    count += 1

def interleave(word1, word2):
  """Interleaves the characters of two words."""
  index = 0
  result = ''
  if len(word1) >= len(word2):
    word = word2
  else:
    word = word1
  while index < len(word):
    char1 = word1[index]
    char2 = word2[index]
    result = result + char1 + char2 
    index += 1
  if len(word1) > len(word2):
     phrase = word1[index:]
     result = result + phrase
  else:
     phrase = word2[index:]
     result = result + phrase
  return result

def pyramid(char, size):
  """Prints a pyramid of the given char with a base of the given size."""
  if size % 2 == 0:
    num = (size - 2) / 2
  else:
    num = (size - 1) / 2
  result = int(num) * ' '
  count = 1
  while count <= size:
    variable = count * char
    variable = result + variable + result
    num = num - 1
    result = int(num) * ' ' 
    count += 2
    print(variable)

def sum_numbers(numbers):
  """Sums the numbers, where numbers are separated by spaces."""
  result = ''
  sum1 = 0
  index = 0
  while index < len(numbers):
    num = numbers[index]
    if num != ' ':
      result = result + str(num)
      if index == len(numbers) - 1:
        sum1 = sum1 + int(result)
    else:
      sum1 = sum1 + int(result)
      result = ''
    index += 1 
  return sum1

def condense(string):
  """Encodes the string based on repetitions of its characters."""
  new_string = ''
  index = 0
  count = 0
  char = string[0]
  while index < len(string):
    letter = string[index]
    if letter == char:
      count += 1    
    else:
      new_string = new_string + char + str(count)
      count = 1
      char = letter
    index += 1
  new_string = new_string + char + str(count)
  return new_string

### BONUS PROBLEMS ###

def number_finder(code, number):
  """Finds the first occurrence of the number in the given code string."""
  index = 0
  new_num = str(number)
  value = 0
  for num in code:
    current_int = new_num[value]
    if len(new_num) != 1:
      if num == current_int:
        value += 1
        index += 1
        if value == (len(new_num)- 1):
          return index - value  
      else:
        value = 0
        index += 1
    else:
      if num == current_int:
        return index
      else:
        index += 1
  return -1

def reverse_vowels(word):
  """Reverses the vowels in the word."""
  result = ''
  result2 = ''
  vowels ='aeiou'
  for letter in word:
    if letter in vowels:
      result = result + letter
  index = len(result) - 1
  for letter in word:
    if letter in vowels:
      result2 = result2 + result[index] 
      index -= 1
    else:
      result2 = result2 + letter  
  return result2

def triforce(char, size):
  """Prints a triforce of the given character with the given size."""
  if size % 2 == 0:
    num = size - 1
    num2 = int(size / 2)
  else:
    num = size
    num2 = size - int(size / 2)
  result = num * ' '
  result2 = num2 * ' ' 
  count = 1
  count2 = 1
  while num >= 0:
    variable = count * char
    if len(variable) <= size:
      variable = result + variable + result
      count += 2      
    else:
      variable = count2 * char
      variable = result + variable + result2 + result + variable
      num2 = num2 - 1
      result2 = num2 * ' ' 
      count2 += 2  
    num = num - 1
    result = num * ' '    
    print(variable)

def sum_word_lengths(words):
  """Sums the lengths of all words.

  Args:
    words: A list of words.

  Returns:
    The sum of the lengths of all of
    the words in the list.
  """
  sum_words = 0
  for word in words:
    # Adds all the lengths of the words.
    sum_words += len(word)
  return sum_words
  
def markdown(menu, discount):
  """Reduces the price of all menu items.

  Args:
    menu: A dictionary of food items to price.
    discount: The amount to reduce the price by.

  Returns:
    The original menu with the price of each
    item reduced by the given discount.
  """
  for key in menu:
    # Access all the prices and subtracts the discount.
    menu[key] = menu[key] - discount
  return menu

def is_key_or_value(string, dictionary):
  """Checks if the given string is a key or value in the dictionary.

  Args:
    string: The string to search for.
    dictionary: A dictionary of strings to strings.

  Returns:
    True if the given string is either a key OR a
    value in the dictionary. Otherwise, False.
  """
  for key in dictionary:
    # Checks to see if string is a key or a value.
    if key == string or dictionary[key] == string:
      return True
  return False

def remove_vowels(word):
  """Removes all vowels from the given word.

  Args:
    word: A lowercase word.

  Returns:
    The given word with all vowels removed,
    where vowels are a, e, i, o, and u.
  """
  new_word = ''
  for char in word:
    # Accumulates string if character is not a vowel.
    if char not in 'aeiou':
      new_word = new_word + char
  return new_word

def blackout(pixels, n):
  """Blacks out the first n rows in the image.

  Args:
    pixels: A 2D list of grayscale pixels.
    n: The number of rows to black out.

  Returns:
    The 2D list with all of the pixels in
    the first n rows changed to black.
  """
  for row in range(0, n):
    # Changes pixel to zero if row is less or equal to n.
    for col in range(0, len(pixels[row])):
      pixels[row][col] = 0
  return pixels
  
  
  
  







