class Solution:
    # Recursively calculates the sum of all numbers from 1 to 'num'
    def sumOfNums(self, num: int) -> int:
        # If num is 0, return 0
        if num == 0:
            return 0

        # If num is 1, return 1
        if num == 1:
            return 1

        # Recursively add current number to the sum of (num - 1)
        return num + self.sumOfNums(num - 1)

solution = Solution()
print(solution.sumOfNums(5))  # Output: 15
