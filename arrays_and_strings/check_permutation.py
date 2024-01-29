# Given two strings, write a method to decide if one is a permutation of the other.


class Solution:

  def check_permutation(self, s, t) -> bool:
    s_map = {}
    t_map = {}

    for char in s:
      s_map[char] = s_map.get(char, 0) + 1

    for char in t:
      t_map[char] = t_map.get(char, 0) + 1

    if s_map == t_map:
      return True

    return False
