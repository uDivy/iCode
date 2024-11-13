class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Check if n is greater than 0 and if it is a power of two
        return n > 0 and (n & (n - 1)) == 0  # Using bitwise operation
        