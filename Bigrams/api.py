import json
import random
import requests


def get_random_key(dictionary):
  """Retrieves a random key from the given dictionary.
  
  Args:
    dictionary: An arbitrary dictionary.
  
  Returns:
    A key selected at random from the dictionary.
  """
  # Put all the dictionary keys into a list.
  keys_as_list = list(dictionary.keys())

  # Generate a random index into the list of keys.
  index = random.randint(0, len(keys_as_list) - 1)

  # Access the key at the randomly generated index.
  return keys_as_list[index]


def get_tracks_for_artist(artist, max_songs):
  """Fetches a list of tracks for the given artist.
  
  Args:
    artist: The artist name.
    max_songs: The maximum number of songs to fetch.
  
  Returns:
    A list of song titles for the given artist,
    as retrieved from the iTunes Search API.
  """
  url = 'https://itunes.apple.com/search?entity=song&limit=' + str(max_songs) + '&term=' + artist.lower()
  response = requests.get(url)

  if response.status_code != 200:
    # Could not find any songs for the given artist.
    print('ERROR: artist "' + artist + '" not found.')
    return []

  results = json.loads(response.text)['results']

  # Collect all the song titles from the API response.
  tracks = []
  for track in results:
    title = track['trackName']

    if ' (feat.' in title:
      # Remove the artist feature from the
      # song title (e.g. change
      # 'We Are (feat. Nas)' to 'We Are').
      title = title[:title.index(' (feat.')]
    
    tracks.append(title)

  return list(set(tracks))


def get_lyrics_for_song(song, artist):
  """Fetches the lyrics for the given song.
  
  Args:
    song: The song title. Spelling and case sensitive.
    artist: The artist name. Spelling and case sensitive.

  Returns:
    A list of the words in the lyrics for the given
    song, in order,  as retrieved from the lyrics.ovh
    API.
  """
  url = 'https://api.lyrics.ovh/v1/' + artist + '/' + song
  response = requests.get(url)

  if response.status_code != 200:
    # Could not find the lyrics for the given
    # song and artist.
    print('...lyrics for "' + song + '" not found')
    return []

  # Convert all the lyrics to lowercase for
  # consistency and split the lyrics into a
  # list of words.
  lyrics = json.loads(response.text)['lyrics']
  return lyrics.lower().split()
