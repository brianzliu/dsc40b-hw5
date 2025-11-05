def mode(numbers):
  """Return a mode (most frequent value) from an iterable of numbers.

  The homework definition allows any of the equally frequent values to be
  returned when there are multiple modes.

  >>> mode([4, 5, 8, 3, 4, 2, 4, 5, 5, -2]) in (4, 5)
  True
  >>> mode([7, 7, 7])
  7
  >>> mode([-1, -1, -2, -3, -1, -2])
  -1
  >>> mode([1])
  1
  """
  """Return a mode from the list of numbers."""
  if not numbers:
    return None 

  n = len(numbers)
  freq = {}
  max_count = 0
  max_value = None
  second_max = 0 

  for i, num in enumerate(numbers):
    count = freq.get(num, 0) + 1
    freq[num] = count

    if count > max_count:
      second_max = max_count
      max_count = count
      max_value = num
    elif count > second_max:
      second_max = count

    remaining = n - (i + 1)
    if remaining + second_max <= max_count:
      return max_value 

  return max_value 