# Implement a method to perform a basic tring
# compression using the counts of repeated characters.
# For exemple, the string aabcccccaaa would become a2b1c5a3.
# If the "compressed" string would not become smaller
# than the original string, your method shoud return the original string.
# You can assume the string has only uppercase and lowcase letters (a - z).


class Solution:

  def string_compression(self, word):
    # Initialize an empty list to store compressed characters and counts
    compressed = []

    # Initialize variables to keep track of the current character and its count
    temp_char = word[0]
    count = 1

    # Iterate through the characters in the input word starting from the second character
    for i in range(1, len(word)):
      # If the current character is the same as the previous one, increment the count
      if word[i] == word[i - 1]:
        count += 1
      else:
        # If the current character is different,
        # append the previous character and its count to the compressed list
        compressed.append(temp_char)
        compressed.append(str(count))
        # Reset the count and update the current character
        count = 1
        temp_char = word[i]

    # Append the last character and its count to the compressed list
    compressed.append(temp_char)
    compressed.append(str(count))

    # Combine the compressed list into a string
    compressed = ''.join(compressed)

    # Check if the compressed string is shorter than the original string
    if len(compressed) > len(word):
      # If not, return the original string
      return word

    # Otherwise, return the compressed string
    return compressed
