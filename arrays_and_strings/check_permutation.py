# Given two strings, write a method to decide if one is a permutation of the other.


class Solution:

  def check_permutation(self, s, t) -> bool:
    # Initialize frequency maps for characters in both strings
    s_map = {}
    t_map = {}

    # Populate frequency map for string s
    for char in s:
      s_map[char] = s_map.get(char, 0) + 1

    # Populate frequency map for string t
    for char in t:
      t_map[char] = t_map.get(char, 0) + 1

    # Check if the frequency maps are equal, indicating a permutation
    if s_map == t_map:
      return True

    # If frequency maps are not equal, strings are not permutations
    return False
