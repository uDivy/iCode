# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # Write your code here.
	prev = head
	on = head.next
	while on is not None:
		later = on.next
		on.next = prev
		prev = on
		on = later
	head.next = None
	head = prev	
	return head