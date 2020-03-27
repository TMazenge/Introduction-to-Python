def load_movie_data():
  """Loads movie data from a text file into a list of movie records.

  Returns:
    A list of movie records of the form [
      title,
      year,
      rating,
      running time,
      genre,
      director,
      [actors],
      score,
    ]
  """
  movies = []
  with open('movies.txt') as f:
    for line in f:
      fields = line.strip('\n').split(',')

      # Convert the numeric fields to integers.
      fields[1] = int(fields[1])  # year
      fields[3] = int(fields[3])  # running time
      fields[7] = int(fields[7])  # score

      # Split the actors string into a list.
      fields[6] = fields[6].split('+')

      movies.append(fields)

  # 'movies' is a list of records of the form:
  # [title, year, rating, running time, genre, director, [actors], score]
  return movies
