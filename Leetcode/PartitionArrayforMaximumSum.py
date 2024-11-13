class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """
        Calculate the maximum sum after partitioning the array.

        Time Complexity:
        - The recursive function `rec` is called for each index in the array, leading to O(n) calls.
        - For each call, we iterate up to `k` (at most) to explore partitions, resulting in O(k) work per call.
        - Therefore, the overall time complexity is O(n * k).

        Space Complexity:
        - The space used by the memoization dictionary is O(n) in the worst case, where each index is stored.
        - The recursion stack can go as deep as O(n) in the worst case.
        - Thus, the overall space complexity is O(n).
        """
        
        memo = {}  # Initialize a memoization dictionary
        
        def rec(index: int) -> int:
            if index in memo:  # Check if the result is already computed
                return memo[index]
            
            # Base case: if we've reached the end of the array
            if index >= len(arr):
                return 0
            
            max_sum = 0
            max_val = 0
            
            # Iterate up to k length for partitioning
            for length in range(1, k + 1):
                if index + length - 1 < len(arr):  # Ensure we don't go out of bounds
                    max_val = max(max_val, arr[index + length - 1])  # Update max in the current partition
                    current_sum = max_val * length + rec(index + length)  # Calculate sum for this partition
                    max_sum = max(max_sum, current_sum)  # Update max_sum
            
            memo[index] = max_sum  # Store the computed result in memo
            return max_sum
        
        return rec(0)  # Start recursion from index 0
