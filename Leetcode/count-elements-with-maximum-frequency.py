from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        self.my_list = [0] * 101  # Create a list of size 101 initialized with zeros
        maxF = 0  # Initialize maxF with 0
        # count = {}  # Initialize count as a dictionary
        
        for num in nums:
            self.my_list[num] += 1  # Update frequency in my_list
            maxF = max(maxF, self.my_list[num])  # Update maxF
            # count[num] = count.get(num, 0) + 1  # Update count dictionary
        return maxF * len([k for k in self.my_list if k == maxF])  # Return maxF times the length of keys with value == maxF