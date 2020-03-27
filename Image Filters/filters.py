import math

def sepia_transform(red, green, blue):
  """Sepiafies the R, G, and B brightness values.

  Args:
    red: The red brightness value of the pixel.
    green: The green brightness value of the pixel.
    blue: The blue brightness value of the pixel.

  Returns:
    A list of the given R, G, and B values transformed
    to a sepia tone.
  """
  new_red = min(math.floor(red * .393 + green * .769 + blue * .189), 255)
  new_green = min(math.floor(red * .349 + green * .686 + blue * .168), 255)
  new_blue = min(math.floor(red * .272 + green * .534 + blue * .131), 255)

  return [new_red, new_green, new_blue]