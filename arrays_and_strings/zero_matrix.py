# Problem:
# Write an algorithm such that if an element in an MxN 
# matrix is 0, its entire row and column are set to 0.

# Input:
# [[3, 5, 6, 0],
#  [2, 0, 3, 0],
#  [9, 2, 7, 1]]

# Output:
# [[0, 0, 0, 0],
#  [0, 0, 0, 0],
#  [9, 0, 7, 0]]

class Solution:
  def zero_matrix(self, matrix):
    # Initialize sets to keep track of rows and columns with 0
    rows_set = set()
    columns_set = set()

    # Identify rows and columns containing 0
    for row in range(len(matrix)):
      for column in range(len(matrix[0])):
        if matrix[row][column] == 0:
          rows_set.add(row)
          columns_set.add(column)

    # Set rows to 0
    for row in rows_set:
      for i in range(len(matrix[0])):
        matrix[row][i] = 0

    # Set columns to 0
    for column in columns_set:
      for i in range(len(matrix)):
        matrix[i][column] = 0

    return matrix
