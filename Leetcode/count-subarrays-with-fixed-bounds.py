class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        left = 0
        min_pos = -1
        max_pos = -1
        
        for right in range(len(nums)):
            if nums[right] < minK or nums[right] > maxK:
                left = right + 1  # Reset the left pointer
                min_pos = -1
                max_pos = -1
            if nums[right] == minK:
                min_pos = right
            if nums[right] == maxK:
                max_pos = right
            
            # The valid subarray starts from the left pointer to the right pointer
            count += max(0, min(min_pos, max_pos) - left + 1)
        
        return count
        