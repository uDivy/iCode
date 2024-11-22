class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(i, j):
            # Check for out of bounds and if the cell is '1'
            if i < 0 or i >= len(land) or j < 0 or j >= len(land[0]) or land[i][j] != 1:
                return
            # Mark the cell as visited by changing '1' to '2'
            land[i][j] = 2
            # Update the boundaries of the farmland
            nonlocal min_row, min_col, max_row, max_col
            min_row = min(min_row, i)
            min_col = min(min_col, j)
            max_row = max(max_row, i)
            max_col = max(max_col, j)
            # Explore all four directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        result = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    min_row, min_col, max_row, max_col = i, j, i, j
                    dfs(i, j)  # Call DFS for each unvisited farmland
                    result.append([min_row, min_col, max_row, max_col])  # Append the boundaries of the farmland
        return result
        