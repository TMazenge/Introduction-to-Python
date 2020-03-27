import database

def find_movies_by_genre(movies, genre):
    """Finds all movies of the given genre.

    Args:
      movies: All the movie records in the database.
      genre: The genre to search for.

    Returns:
      A list of all the movie titles of movies that
      belong to the given genre.
    """
    results = []
    for movie in movies:
      if genre == movie[4]:
        # Only include the movie title in the results.
        results.append(movie[0])
    return results

def find_movies_by_min_score(movies, min_score):
    """Finds all movies with a score above the given min score.

    Args:
      movies: All the movie records in the database.
      min_score: The minimum score desired.

    Returns:
      A list of all the movie titles of movies that
      have a score greater than or equal to the given
      score.
    """
    result = []
    for movie in movies:
      #Only include movie title for movie with score greater than or equal to the min_score
      if min_score <= movie[7]:
        result.append(movie[0])
    return result

def find_movies_by_keyword(movies, keyword):
    """Finds all movies with the given keyword in the title.

    Args:
      movies: All the movie records in the database.
      keyword: The keyword to look for in the movie title.

    Returns:
      A list of all the movie titles of movies that
      have the given keyword somewhere in the title.
    """
    result = []
    for movie in movies:
      if keyword in movie[0]:
        #Adds all the movies if the keyword is in the title
        result.append(movie[0])
    return result

def avg_running_time_by_year(movies, year):
    """Calculates the average running time for movies released in the given year.

    Args:
      movies: All the movie records in the database.
      year: The release year to search for.

    Returns:
      A list of all the movie titles of movies that
      were released in the given year.
    """
    result = []
    sum_of_time = 0
    for movie in movies:
      if year == movie[1]:
        #Adds the running time of all movies in the given year
        sum_of_time = sum_of_time + movie[3]
        result.append(movie[1])
    #Finds the average of all the running time
    if result != []:
      average_time = sum_of_time / len(result) 
    else:
      average_time = 0 
    return average_time 

#Finds the index of the given rating
def find_index(word_rating):
    if word_rating == 'G':
      index = 0
    elif word_rating == 'PG':
      index = 1
    elif word_rating == 'PG-13':
      index = 2
    elif word_rating == 'R':
      index = 3
    elif word_rating == 'NC-17':
      index = 4
    return index
    
def find_movies_by_max_rating(movies, max_rating):
    """Finds all movies with the given MCAA rating or below.

    Args:
      movies: All the movie records in the database.
      max_rating: The max desired MCAA rating.

    Returns:
      A list of all the movie titles of movies that
      have an MCAA rating at or below the given rating.
      MCAA ratings are ordered from lowest to highest as:
      G, PG, PG-13, R, NC-17.
    """
    result = []
    #Index of the given rating 
    index = find_index(max_rating)
    for movie in movies:
      current_rating = movie[2]
      #Checks to see if index of movie is greater than the index of the given rating
      if find_index(current_rating) <= index:
        #Add all the movies with indices less or equal to the index of the given rating
        result.append(movie[0])
    return result
    
  
def find_movies_by_keyword_and_min_score(movies, keyword, min_score):
    """Finds all movies with the given keyword and above the given score.

    Args:
      movies: All the movie records in the database.
      keyword: The keyword to looks for in the movie title.
      min_score: The minimum score desired.

    Returns:
      A list of all the movie titles of movies that
      both contain the give keyword in their title
      and have a score greater than or equal to the
      given score.
    """
    result = []
    for movie in movies:
      #Checks to see if keyword in movir title and movie score is greater than the min_score
      if keyword in movie[0] and min_score < movie[7]:
        result.append(movie[0])
    return result

def search(movies):
  """Searches the movies records based on the user's search terms."""
  print('WELCOME TO FISK IMDb!')

  movie_genre = input('\nSearch by genre: ')
  print(find_movies_by_genre(movies, movie_genre))

  minimum_score = int(input('\nSearch by minimum score: '))
  print(find_movies_by_min_score(movies, minimum_score))

  title_keyword = input('\nSearch by keyword: ')
  print(find_movies_by_keyword(movies, title_keyword))

  print('\nSearch by keyword "' + title_keyword + '" and min score "' + str(minimum_score) + '":')
  print(find_movies_by_keyword_and_min_score(movies, title_keyword, minimum_score))

  release_year = int(input('\nSearch by release year: '))
  print('Average running time: ' + str(avg_running_time_by_year(movies, release_year)))

  max_mcaa_rating = input('\nSearch by max MCAA rating: ')
  print(find_movies_by_max_rating(movies, max_mcaa_rating))


# Load our movie database and search through it.
movie_records = database.load_movie_data()
search(movie_records)