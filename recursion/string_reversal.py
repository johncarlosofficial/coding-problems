from typing import Optional

# Solution1 class implements string reversal using recursion and a helper function
class Solution1:
    # This method reverses a given string using recursion
    def reverseString(self, word: str) -> str:
        # Initialize an empty string to store the reversed result
        reversed = ""

        # Helper function to handle recursion
        def helper(a):
            # 'nonlocal' allows access to the 'reversed' variable from the outer scope
            nonlocal reversed
            # Base case: when the string is empty, stop recursion
            if not a:
                return ""
            
            # Add the last character of the string to the 'reversed' string
            reversed += a[-1]

            # Call the helper function with the string minus its last character
            return helper(a[:-1])

        # Start the recursion by calling the helper function
        helper(word)

        # Return the reversed string after the recursion finishes
        return reversed

# Solution2 class implements string reversal using recursion in a more direct approach
class Solution2:
    # This method reverses a given string using recursion without needing a helper function
    def reverseString(self, string: Optional[str]) -> str:
        # Base case: if the string is empty, return an empty string
        if not string:
            return ""

        # Add the last character of the string to the reversed part
        # Recursively call the function with the remaining string (excluding the last character)
        return string[-1] + self.reverseString(string[:-1])

# Create an instance of Solution1 and reverse the string "abcd"
solution1 = Solution1()
print(solution1.reverseString("abcd"))  # Output: "dcba"

# Create an instance of Solution2 and reverse the string "abcd"
solution2 = Solution2()
print(solution2.reverseString("abcd"))  # Output: "dcba"
