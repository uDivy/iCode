class Solution:
    def maxDepth(self, s: str) -> int:
        left_count = 0
        max_depth = 0
        
        for char in s:
            if char == '(':
                left_count += 1
                max_depth = max(max_depth, left_count)
            elif char == ')':
                left_count -= 1
        
        return max_depth
        