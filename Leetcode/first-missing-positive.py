class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Create a set to store positive integers
        num_set = set(nums)
        # Initialize the smallest missing positive integer
        missing = 1
        
        while missing in num_set:
            missing += 1
        
        return missing