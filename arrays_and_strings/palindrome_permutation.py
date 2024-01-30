# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.

# EXEMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco cta", etc.)

# To be a palindrome, all letters should
# repeat n%2 == 0 and or just one sould repeat n%2 == 1


class Solution:

  def palindrome_permutation(self, s: str) -> bool:
    # Convert the input string to lowercase for case-insensitive comparison
    s = s.lower()

    # Initialize a dictionary to store character counts
    char_count_map = {}

    # Count the occurrences of each character (excluding spaces) in the string
    for char in s:
      if char != " ":
        char_count_map[char] = char_count_map.get(char, 0) + 1

    # Extract the character counts from the dictionary into a list
    char_count_list = list(char_count_map.values())

    # Initialize a variable to count the number of characters with odd counts
    odd_count = 0

    # Check if the characters can form a palindrome permutation
    for count in char_count_list:
      if count % 2 == 1:
        odd_count += 1

        # If more than one character has an odd count, it cannot be a palindrome
        if odd_count == 2:
          return False

    # If the code reaches this point, the string can be a permutation of a palindrome
    return True
