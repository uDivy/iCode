from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1  # Initialize two pointers
        result = [0] * len(nums)  # Initialize an empty array of the same size as nums
        
        # Fill the result array from the rightmost position
        for i in range(len(nums) - 1, -1, -1):
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            
            if left_square > right_square:
                result[i] = left_square
                left += 1
            else:
                result[i] = right_square
                right -= 1
        return result
        