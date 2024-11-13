# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        from collections import deque
        
        def bfs():
            queue = deque([(root, 0)])  # Initialize queue with root and its level
            
            while queue:
                level_size = len(queue)
                level_values = []  # Reset level values for each level
                
                for _ in range(level_size):
                    node, level = queue.popleft()
                    
                    if level % 2 == 0:
                        # Check for odd values and strictly increasing
                        if node.val % 2 == 0 or (level_values and node.val <= level_values[-1]):
                            return False
                    else:
                        # Check for even values and strictly decreasing
                        if node.val % 2 != 0 or (level_values and node.val >= level_values[-1]):
                            return False
                    
                    level_values.append(node.val)
                    
                    # Add children to the queue
                    if node.left:
                        queue.append((node.left, level + 1))
                    if node.right:
                        queue.append((node.right, level + 1))
            
            return True
        
        return bfs()
        