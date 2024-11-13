class Solution:
    def numSquares(self, n: int) -> int:
        """
        Returns the least number of perfect square numbers which sum to n.

        Time Complexity: O(n * sqrt(n))
        - The outer loop runs n times, and the inner loop runs up to sqrt(n) times.

        Space Complexity: O(n)
        - We use a list of size n + 1 to store the minimum counts for each number up to n.
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case
        
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]
        