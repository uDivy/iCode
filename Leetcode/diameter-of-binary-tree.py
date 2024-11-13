# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # Initialize diameter

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_depth = dfs(node.left)  # Depth of left subtree
            right_depth = dfs(node.right)  # Depth of right subtree
            
            # Update the diameter if the path through the current node is larger
            self.diameter = max(self.diameter, left_depth + right_depth)
            
            return max(left_depth, right_depth) + 1  # Return the depth of the tree

        dfs(root)  # Start DFS from the root
        return self.diameter  # Return the maximum diameter found
        