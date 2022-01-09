# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    node = head
    count = 0


    while node is not None:
        count += 1
        node = node.next

    pos = (count - k) + 1

    if pos == 1:
        head.value = head.next.value
        head.next = head.next.next
        return

    curr_node = head
    for i in range(1, pos - 1):
        curr_node = curr_node.next

    nxt_node = curr_node.next

    curr_node.next = nxt_node.next