# There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit
# (or zero edits) away.

# Example:
# - "pales" and "pale" are one edit away (remove 's')
# - "pale" and "bale" are one edit away (replace 'p' with 'b')
# - "pale" and "bake" are not one edit away
# - "pale" and "ple" are one edit away (remove 'a')


class Solution:

  def one_away(self, str1, str2):
    # If the strings are already equal, no edits are needed.
    if str1 == str2:
      return True

    # If the difference in lengths is greater than 1, more than one edit is required.
    if abs(len(str1) - len(str2)) > 1:
      return False

    # Make sure str1 is the longer string (or equal length if they are the same).
    if len(str1) < len(str2):
      str1, str2 = str2, str1

    # Initialize variables for tracking edits and indices.
    edits = 0
    i, j = 0, 0

    # Iterate through the characters of both strings.
    while i < len(str1) and j < len(str2):
      # If characters at the current indices are different, an edit is needed.
      if str1[i] != str2[j]:
        edits += 1

        # If the strings are of equal length, move to the next character
        # in the shorter string.
        if len(str1) == len(str2):
          j += 1
      else:
        # Move to the next character in both strings if characters are equal.
        j += 1

      # Move to the next character in the longer string.
      i += 1

    # Check if the total edits are at most one.
    return edits <= 1
