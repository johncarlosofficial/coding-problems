class Solution:
    # Method to calculate the Fibonacci number at a given position using recursion
    def fibonacci(self, position):
        # Base case: the Fibonacci number at position 0 is 0
        if position == 0:
            return 0
        
        # Base case: the Fibonacci number at position 1 is 1
        if position == 1:
            return 1

        # Recursive case: sum of the two previous Fibonacci numbers
        return self.fibonacci(position - 1) + self.fibonacci(position - 2)

solution = Solution()

# Testing the method with position 6 (fibonacci sequence: 0, 1, 1, 2, 3, 5, 8)
print(solution.fibonacci(6))  # Output: 8
