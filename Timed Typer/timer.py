import select
import sys

def input_with_timeout(seconds):
  """Waits for the user to enter a value, with a time limit.

  Args:
    seconds: Seconds before the prompt times out.

  Returns:
    The value the user entered. If the user did not
    enter a value within the time limit, returns the
    empty string.
  """
  response, _, _ = select.select([sys.stdin], [], [], seconds)
  if response:
    return sys.stdin.readline().strip()
  else:
    return ''