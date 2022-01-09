# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    head = linkedList
    prev = head
    curr = head.next
    while curr is not None:
        if prev.value == curr.value:
            curr = curr.next
            prev.next = curr
        else:
            prev = curr
            curr = curr.next


    return linkedList
