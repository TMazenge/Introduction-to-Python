import filters

### GRAYSCALE IMAGE FILTERS ###

def make_negative(pixels):
  """Converts a grayscale image to its negative.
  
  Args:
    pixels: A 2D list of grayscale pixels.

  Returns:
    A 2D list of pixels that represent the negative
    of the original image.
  """
  for row in range(0, len(pixels)):
    for col in range(0, len(pixels[row])):
      #Give the inverse of the pixel
      pixels[row][col] = 255 - pixels[row][col]
  return pixels

def posterize(pixels, bucket_size):
  """Posterizes a grayscale image.
  
  Args:
    pixels: A 2D list of grayscale pixels.
    bucket_size: The size of the brightness bucket.

  Returns:
    A 2D list of pixels that represent a posterized
    version of the original image.
  """
  for row in range(0, len(pixels)):
    for col in range(0, len(pixels[row])):
      pixel = pixels[row][col]
      #If less than bucket_size pixel is changed to 0
      if pixel < bucket_size:
        pixels[row][col] = 0
      else:
        #Bucket_size is increased by a factor of one and checks if pixel false in range of new bucket size 
        curr_bucket = bucket_size * 2
        for curr_bucket in range(curr_bucket, 255 + bucket_size, bucket_size):
          if pixel < curr_bucket:
            pixels[row][col] = curr_bucket - bucket_size
            break
  return pixels
 

### RGB COLOR IMAGE FILTERS ###

def darken(pixels, amount):
  """Darkens a color image.

  Args:
    pixels: A 3D list of RGB pixels.
    amount: Brightness amount to darken the image by.

  Returns:
    A 3D list of pixels that represent a darkened
    version of the original image.
  """
  for row in range(0, len(pixels)):
    for col in range(0, len(pixels[row])):
      for rgb in range(0, 3):
        #Subtract amount from all rgb values and if the difference is less than zero pixel is assigned to zero
        if pixels[row][col][rgb] - amount < 0:
          pixels[row][col][rgb] = 0
        else:
          pixels[row][col][rgb] = pixels[row][col][rgb] - amount
  return pixels

def add_border(pixels, width):
  """Adds a border to a color image.

  Args:
    pixels: A 3D list of RGB pixels.
    width: The number of pixels wide to make the border.

  Returns:
    A 3D list of pixels that represent the original
    image with a border around it.
  """
  for row in range(0, len(pixels)):
    for col in range(0, len(pixels[row])):
      for rgb in range(0, 3):
        #Checks to see where the edge will start towards the end of the row
        last_row  = (len(pixels) - 1) - width
        if row < width or row > last_row:
          pixels[row][col][rgb] = 0
        #Checks to see where the edge will start towards the end of the col 
        last_col = (len(pixels[row]) - 1) - width
        if col < width or col > last_col:
          pixels[row][col][rgb] = 0   
  return pixels 

def sepiafy(pixels):
  """Recolors a color image in sepia tones.
  
  Args:
    pixels: A 3D list of RGB pixels.

  Returns:
    A 3D list of pixels that represent the original
    image with a sepia filter.
  """
  # Use the sepia_transform() function from the
  # filters module.
  for row in range(0, len(pixels)):
    for col in range(0, len(pixels[row])):
      #Changes all rgb values to a sepia values
      new_col = filters.sepia_transform(pixels[row][col][0], pixels[row][col][1], pixels[row][col][2])
      pixels[row][col] = new_col
  return pixels
  