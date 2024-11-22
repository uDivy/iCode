# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        mid = self.findMid(head)
        first = head
        second = self.reverse(mid)

        while second:
            temp = first.next
            first.next = second
            first = temp

            temp = second.next
            second.next = first
            
            second = temp if first else None
        
        return head

    def findMid(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev