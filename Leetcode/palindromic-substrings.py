class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Time Complexity:
        O(n^2): We iterate through all possible substrings, where n is the length of the string.
        Each substring check involves a constant-time operation due to the DP table.

        Space Complexity:
        O(n^2): We use a 2D DP table of size n x n to store whether substrings are palindromic.
        """
        n = len(s)
        count = 0
        dp = [[False] * n for _ in range(n)]

        # Base case: Single character palindromes
        for i in range(n):
            dp[i][i] = True
            count += 1  # Each single character is a palindrome

        # Base case: Two character palindromes
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1  # Count this pair as a palindrome

        # Check for palindromes of length greater than 2
        for length in range(3, n + 1):  # Length of substring
            for start in range(n - length + 1):  # Start index
                end = start + length - 1  # End index
                if s[start] == s[end] and dp[start + 1][end - 1]:  # Check boundaries
                    dp[start][end] = True
                    count += 1  # Count this substring as a palindrome

        return count  # Return the total number of palindromic substrings


