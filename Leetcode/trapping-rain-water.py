class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        water_trapped = 0
        
        # Calculate next greater to left
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i - 1])
        
        # Calculate next greater to right
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i + 1])
        
        # Calculate water trapped
        for i in range(n):
            water_trapped += max(0, min(left_max[i], right_max[i]) - height[i])
        
        return water_trapped