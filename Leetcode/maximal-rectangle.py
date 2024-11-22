class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        # Initialize heights for histogram
        heights = [0] * len(matrix[0])
        max_area = 0
        
        for row in matrix:
            for i in range(len(row)):
                # Update heights
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            # Calculate max area for the current histogram
            max_area = max(max_area, self.maxHistogramArea(heights))
        
        return max_area

    def maxHistogramArea(self, heights: List[int]) -> int:
        # NGEL and NGER technique to find max area in histogram
        n = len(heights)
        left = [0] * n
        right = [0] * n
        stack = []
        
        # Find NGEL
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack.clear()
        
        # Find NGER
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        # Calculate max area
        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            max_area = max(max_area, heights[i] * width)
        
        return max_area
        