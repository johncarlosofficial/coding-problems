# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


class Solution:

  def is_unique(self, s):
    group = set()

    for char in s:
      if char not in group:
        group.add(char)
      else:
        return False

    return True
