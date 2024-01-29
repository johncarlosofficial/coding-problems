# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end
# to hold the additional characters, and that you are given the
# "true" length of the string. (Note: If implementing in Java,
# please use a character array so that you can perform this
# operation in place)


class Solution:
  def urlify(self, s: str) -> str:
    words = []
    for char in s:
      if char != " ":
        words.append(char)
      else:
        words.append("%20")

    ans = ''.join(words)

    return ans