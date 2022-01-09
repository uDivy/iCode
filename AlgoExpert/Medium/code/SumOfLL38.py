# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    nodeOne = linkedListOne
    nodeTwo = linkedListTwo

    mul = 1
    num1, num2 = 0, 0
    while nodeOne is not None or nodeTwo is not None:
        if nodeOne is not None:
            num1 += mul * nodeOne.value
            nodeOne = nodeOne.next
        if nodeTwo is not None:
            num2 += mul * nodeTwo.value
            nodeTwo = nodeTwo.next

        mul *= 10

    sol = num1 + num2
    arr = list(map(int, str(sol)))
    head = LinkedList(arr[-1])
    node = head
    for val in reversed(arr[:-1]):
        node.next = LinkedList(val)
        node = node.next


    return head
