# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # Initialize the queue and push the root node
        queue = [root]
        
        # BFS traversal
        while queue:
            node = queue.pop(0)  # Pop the front element
            # Check for right and left children
            if node.right:  # Push right child to queue
                queue.append(node.right)
            if node.left:  # Push left child to queue
                queue.append(node.left)
        
        return node.val  # Return the last node's value
        