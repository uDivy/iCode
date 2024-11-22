class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total = 0
        shared_edges = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    total += 4  # Count all edges
                    if i > 0 and grid[i - 1][j] == 1:  # Check top
                        shared_edges += 1
                    if j > 0 and grid[i][j - 1] == 1:  # Check left
                        shared_edges += 1
        
        return total - 2 * shared_edges  # Subtract shared edges
        