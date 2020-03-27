import api
import random

def get_lyrics_for_artist(artist, max_songs):
  """Creates a dictionary of song title to lyrics.

  Args:
    artist: The artist to look up songs for.
    max_songs: The maximum number of songs to look up.

  Returns:
    A dictionary of lyrics for the given artist,
    where the keys are song titles and the values
    are the lyrics for the song as a list of words.
  """
  lyrics = {}
  list_of_songs = api.get_tracks_for_artist(artist, max_songs)
  for song in list_of_songs:
    # Adds song titles and list of lyrics to dictionary as key and value
    lyrics[song] = api.get_lyrics_for_song(song, artist)
  return lyrics

def get_bigrams_for_song(lyrics):
  """Creates a dictionary of bigrams in a single song.

  Args:
    lyrics: A list of the words in a song's lyrics.

  Returns:
    A dictionary of lyric bigrams, where the keys are
    words and the values are a list of all the words
    that directly follow that word in the lyrics.
  """
  biagrams_of_song = {}
  for index in range(0, len(lyrics) - 1):
    if lyrics[index] in biagrams_of_song:
      # Add word to list which contains other words which complete a biagram pair
      biagrams_of_song[lyrics[index]].append(lyrics[index + 1])
    else:
      # Creates a new key and value of biagram pairs
      biagrams_of_song[lyrics[index]] = [lyrics[index + 1]] 
  return biagrams_of_song

def get_bigrams_for_artist(lyrics_for_artist):
  """Creates a dictionary of bigrams for an artist.
  
  Args:
    lyrics_for_artist: A dictionary of song title to lyrics.
  
  Returns:
    A single dictionary of lyric bigrams for all of the
    artist's songs, where the keys are words and the
    values are a list of all the words that directly
    follow that word in the lyrics.
  """
  biagrams = {}
  lists_of_lyrics = []
  for song_lyrics in lyrics_for_artist.values():
    # Creates lists of dictionaries of biagram pairs as lists
    lists_of_lyrics.append(get_bigrams_for_song(song_lyrics))
  for index in range(0, len(lists_of_lyrics)):
    # Accesses a key and adds all words that follow it into a list as a value
    for key in lists_of_lyrics[index]: 
      if key in biagrams:
        for char in lists_of_lyrics[index][key]:
          biagrams[key].append(char)
      else:
        # Creates a new key if it does not exist
        biagrams[key] = lists_of_lyrics[index][key]
  return biagrams

def make_song(bigrams_for_artist, num_words):
  """Generates a song based on common bigrams.
  
  Args:
    bigrams_for_artist: A dictionary of bigrams for an artist.
    num_words: The number of words in the generated song.
  
  Returns:
    Randomly generated lyrics using the bigrams found in the
    artist's body of work.
  """
  generated_song = ''
  # Gets Random key
  key = api.get_random_key(bigrams_for_artist)
  for num in range(0, num_words):
    first_key = key
    list_of_words = bigrams_for_artist[key]
    # Gets a random index to create a random biagram 
    index = random.randint(0, len(list_of_words) - 1) 
    generated_song = generated_song + key + ' ' 
    # Checks to see if word exist as a key else, the key is set to the first random key
    if list_of_words[index] in bigrams_for_artist:
      key = list_of_words[index]
    else:
      key = first_key
  return generated_song.strip()

def generate_song_for_artist(artist):
  """Generates a song in the style of the given artist.
  
  Args:
    artist: Name of a musical artist.
  
  Returns:
    A song in the style of the given artist randomly
    generated using natural language processing.
  """
  # Look up songs and lyrics for the artist.
  lyrics_by_song = get_lyrics_for_artist(artist, 75)

  # Collect bigrams from the artist's lyrics.
  artist_bigrams = get_bigrams_for_artist(lyrics_by_song)

  # Generate song lyrics using the collected bigrams.
  return make_song(artist_bigrams, 30)
  

  
