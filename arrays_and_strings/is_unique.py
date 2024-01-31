# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


class Solution:

  def is_unique(self, s):
    # Initialize an empty set to track unique characters
    group = set()

    # Iterate through each character in the string
    for char in s:
      # If the character is not in the set, add it
      if char not in group:
        group.add(char)
      # If the character is already in the set, string has duplicate characters
      else:
        return False

    # All characters are unique if the loop completes without returning False
    return True