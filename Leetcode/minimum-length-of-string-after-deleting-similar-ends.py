class Solution:
    def minimumLength(self, s: str) -> int:
        start, end = 0, len(s) - 1
        while start < end and s[start] == s[end]:
            if s[start] == s[end]:
                # Move pointers if characters are the same
                while start < end and s[start] == s[start + 1]:
                    start += 1
                while start < end and s[end] == s[end - 1]:
                    end -= 1
                if start >= end:
                    end -= 1
                    break
                
            # Move both pointers if characters are different
            start += 1
            end -= 1
        return end - start + 1
# Example usage
solution = Solution()
result = solution.minimumLength("cabaabac")
print(result)  # Output the result
        