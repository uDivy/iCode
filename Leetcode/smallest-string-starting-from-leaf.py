# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    smallest_string = ""  # Global variable to keep track of the smallest string

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        # Start DFS from the root
        self.dfs(root, "")
        return self.smallest_string

    def dfs(self, node: Optional[TreeNode], path: str):
        if not node:
            return
        
        # Prepend the current node's character to the path
        path = chr(node.val + ord('a')) + path
        
        # If it's a leaf node, check if the current path is smaller
        if not node.left and not node.right:
            if (self.smallest_string == "" or 
                path < self.smallest_string):
                self.smallest_string = path
        
        # Continue DFS on left and right children
        self.dfs(node.left, path)
        self.dfs(node.right, path)
        