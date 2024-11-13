from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Candidate Selection and Verification Steps
        candidate = None
        count = 0

        # Candidate Selection
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        # Verification
        count = sum(1 for num in nums if num == candidate)
        if count > len(nums) // 2:
            return candidate
        else:
            return None  # or raise an exception if no majority element exists
        