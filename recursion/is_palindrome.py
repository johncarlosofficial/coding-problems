from typing import Optional

# Solution class that provides a method to check if a string is a palindrome
class Solution:
    # This method returns True if the input string is a palindrome, False otherwise
    def isPalindrome(self, s: Optional[str]) -> bool:
        # If the string is empty or None, we consider it a palindrome
        if not s:
            return True

        # Recursive helper function that checks if the string is a palindrome
        def helper(s, left, right):
            # Base case: If the left index crosses the right index, we've checked all characters
            if left > right:
                return True
            # If characters at the current left and right positions don't match, it's not a palindrome
            if s[left] != s[right]:
                return False

            # Recursively check the next pair of characters
            return helper(s, left+1, right-1)

        # Start the recursion with the full string, checking from the first (left) and last (right) characters
        return helper(s, 0, len(s) - 1)

# Create an instance of the Solution class
solution = Solution()

# Test the method with a palindrome string "abcdcba"
print(solution.isPalindrome("abcdcba"))  # Output: True

# Test the method with a non-palindrome string "bea"
print(solution.isPalindrome("bea"))  # Output: False
