class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        freq = {}
        max_length = 0
        count_exceeding_k = 0  # Track how many numbers exceed frequency k
        
        for right in range(len(nums)):
            # Update frequency of the current number
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            
            # Check if the current number's frequency exceeds k
            if freq[nums[right]] == k + 1:
                count_exceeding_k += 1
            
            # Shrink the window if any number's frequency exceeds k
            while count_exceeding_k > 0:
                freq[nums[left]] -= 1
                if freq[nums[left]] == k:
                    count_exceeding_k -= 1
                elif freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            
            # Update maximum length of the window
            max_length = max(max_length, right - left + 1)
        
        return max_length
        