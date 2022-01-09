# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    # Write your code here.
    rootNode = get_height(tree)
    return rootNode.isBal


class parentInfo:
    def __init__(self, isBal, height):
        self.isBal = isBal
        self.height = height


def get_diff(leftChild, rightChild):
    isBal = True
    if abs(leftChild.height - rightChild.height) > 1 or (leftChild.isBal and rightChild.isBal) is False:
        isBal = False
    parentNode = parentInfo(isBal, max(leftChild.height, rightChild.height) + 1)
    return parentNode


def get_height(tree):
    if tree is None:
        return parentInfo(True, -1)

    parentNode = get_diff(get_height(tree.left), get_height(tree.right))
    print(tree.value, parentNode.height)
    return parentNode
