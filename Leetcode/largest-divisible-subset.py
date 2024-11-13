from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        Time Complexity:
            O(n^2) - Sorting the array takes O(n log n), and building the DP array requires 
             O(n^2) due to the nested loop for checking divisibility.

        Space Complexity:
            O(n) - Extra space is used for the `dp` and `prev` arrays to store intermediate 
           results and for backtracking to form the result subset.
        """
        nums.sort()
        n = len(nums)
        dp = [1] * n  # Each element is its own subset initially
        prev = [-1] * n  # Track previous element in the subset for each index
        max_index = 0  # Track the index of the largest subset's last element
        
        for i in range(1, n):
            for j in range(i):
                # dp[i] < dp[j] + 1, it says if adding that element will not increase its size
                # then skip that element
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > dp[max_index]:
                max_index = i

        result = []
        while max_index >= 0:
            result.append(nums[max_index])
            max_index = prev[max_index]
        result.reverse()
        return result


        

        