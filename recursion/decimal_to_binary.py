class Solution:
    def decimalToBinary(self, decimal: int, binary: str = "") -> str:
        # Base case: If decimal is 0, return the accumulated binary string
        # If binary is empty (which means decimal was 0), return "0"
        if decimal == 0:
            return binary if binary else "0"
        
        # Recursive case: Process the number to build the binary representation
        # Compute the current bit (0 or 1) by finding the remainder when decimal is divided by 2
        # Prepend this bit to the current binary string
        current_bit = str(decimal % 2)
        return self.decimalToBinary(decimal // 2, current_bit + binary)

solution = Solution()
print(solution.decimalToBinary(10))