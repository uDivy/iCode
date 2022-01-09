# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    array = []


    findKthLargestValueInBst_rec(tree, array)
    return array[len(array) - k]


def findKthLargestValueInBst_rec(tree, array):
    if tree is None:
        return

    findKthLargestValueInBst_rec(tree.left, array)
    array.append(tree.value)
    findKthLargestValueInBst_rec(tree.right, array)