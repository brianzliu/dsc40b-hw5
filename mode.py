def mode(numbers):
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