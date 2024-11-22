class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sum_freq = {0: 1}  # Initialize with sum 0 having one occurrence
        current_sum = count = 0
        
        for num in nums:
            current_sum += num
            
            # Check if current_sum equals goal
            if current_sum == goal:
                count += 1
            
            # Check if current_sum - goal exists in sum_freq
            if current_sum - goal in sum_freq:
                count += sum_freq[current_sum - goal]
            
            # Update sum_freq with the current_sum
            if current_sum in sum_freq:
                sum_freq[current_sum] += 1
            else:
                sum_freq[current_sum] = 1
        
        return count
