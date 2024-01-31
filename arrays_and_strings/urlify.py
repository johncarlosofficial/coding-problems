# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end
# to hold the additional characters, and that you are given the
# "true" length of the string. (Note: If implementing in Java,
# please use a character array so that you can perform this
# operation in place)


class Solution:

  def urlify(self, s: str) -> str:
    # Initialize an empty list to store characters with space replaced
    words = []

    # Iterate through each character in the input string
    for char in s:
      # If the character is not a space, add it to the list
      if char != " ":
        words.append(char)
      # If the character is a space, replace it with '%20'
      else:
        words.append("%20")

    # Concatenate the characters in the list to form the final string
    ans = ''.join(words)

    # Return the resulting string with spaces replaced by '%20'
    return ans
