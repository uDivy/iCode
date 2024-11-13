class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        # Right shift until left and right are equal
        while left < right:
            left >>= 1
            right >>= 1
            count += 1
        # Left shift the result back by the count
        return left << count
        