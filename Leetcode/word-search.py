class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, word, i, j, index):
            # Base cases will be handled here
            if index == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
                return False
            temp = board[i][j]
            board[i][j] = '#'  # Mark as visited
            # Explore all four directions
            found = (dfs(board, word, i + 1, j, index + 1) or  # Down
                     dfs(board, word, i - 1, j, index + 1) or  # Up
                     dfs(board, word, i, j + 1, index + 1) or  # Right
                     dfs(board, word, i, j - 1, index + 1))    # Left
            if found:
                return True
            board[i][j] = temp  # Unmark the cell
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(board, word, i, j, 0):
                    return True
        return False
        