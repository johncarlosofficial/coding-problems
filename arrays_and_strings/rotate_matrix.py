# Given an image represented by an NxM matrix, where each pixel in the image is 4 bytes,
# write a method to rotate the image by 90 degrees. Can you do this in place?

# Input:
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]

# Output:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]

class Solution:
  def rotate_matrix(self, matrix):
    # Step 1: Transpose the matrix
    # [[1, 4, 7],
    #  [2, 5, 8],
    #  [3, 6, 9]]
    for row in range(len(matrix)):
      for column in range(row, len(matrix[row])):
        matrix[row][column], matrix[column][row] = \
        matrix[column][row], matrix[row][column]

    # Step 2: Reverse each row of the matrix by swapping elements from left to right
    # [[7, 4, 1],
    #  [8, 5, 2],
    #  [9, 6, 3]]
    for row in range(len(matrix)):
      left = 0
      right = len(matrix[row]) - 1
      while left < right:
        matrix[row][left], matrix[row][right] = \
        matrix[row][right], matrix[row][left]
        left += 1
        right -= 1

    return matrix