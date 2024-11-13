# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head  # Initialize slow pointer
        fast = head  # Initialize fast pointer
        while fast and fast.next:  # Check if fast and fast.next are not None
            slow = slow.next  # Move slow pointer 1 step
            fast = fast.next.next  # Move fast pointer 2 steps
            if fast == slow:  # Check if pointers meet
                return True  # Cycle detected
        return False  # No cycle found
        