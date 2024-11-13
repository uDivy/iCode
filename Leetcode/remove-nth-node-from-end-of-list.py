# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize length and a copy of head
        length = 0
        current = head  # Create a copy of head
        
        # Traverse the linked list to find its length
        while current:
            length += 1
            current = current.next

        if length == 1 and n == 1:
            return None
        
        # Calculate the position of the node to remove
        position_to_remove = length - n 
        print(position_to_remove)
        
        # Initialize two pointers
        first = head
        second = first

        for _ in range(position_to_remove):
            second = first
            first = first.next
        
        if first:
            second.next = first.next
        else:
            second.next = None

        return head