class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_len = 0
        freq_map = {0: -1}  # Initialize with count 0 at index -1
        
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1  # Increment for 1, decrement for 0
            if count in freq_map:
                max_len = max(max_len, i - freq_map[count])
            else:
                freq_map[count] = i
        
        return max_len
        