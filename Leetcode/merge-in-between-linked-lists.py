# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Initialize pointers
        current = list1
        prev_a = None
        prev_b = None
        # Traverse list1 to find positions a and b
        for i in range(b + 1):
            if i == a - 1:
                prev_a = current  # Pointer to node before position a
            if i == b:
                prev_b = current  # Pointer to node at position b
            current = current.next
        
        # Connect prev_a to the head of list2
        prev_a.next = list2
        
        # Traverse to the end of list2
        while list2.next:
            list2 = list2.next
        
        # Connect the end of list2 to the node after b
        list2.next = prev_b.next
        
        return list1