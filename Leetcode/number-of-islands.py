class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # Check for out of bounds and if the cell is '1'
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return
            # Mark the cell as visited by changing '1' to '2'
            grid[i][j] = '2'
            # Explore all four directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)  # Call DFS for each unvisited island
                    count += 1  # Increment the island count
        return count
        