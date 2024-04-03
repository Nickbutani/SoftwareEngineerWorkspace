def is_odd_string(word):
    return sum([ord(char) - 96 for char in word.lower()]) % 2 != 0
  
    # Hint: you may find the ord() function useful here