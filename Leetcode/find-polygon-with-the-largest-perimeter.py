from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        maxP = 0
        nums.sort()  # Sort the list first
        prev_sum = nums[0] + nums[1]  # Initialize running sum
        # Start from the third index
        for i in range(2, len(nums)):
            if prev_sum > nums[i]:  # Check if the sum of previous elements is greater
                maxP = max(maxP, prev_sum + nums[i])  # Update maxP if the new perimeter is greater
            prev_sum += nums[i]  # Update running sum by adding the previous element
        return maxP if maxP != 0 else -1