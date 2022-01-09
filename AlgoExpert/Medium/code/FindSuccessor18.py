# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    return rec_code(tree, node, None)


def rec_code(tree, node, val):
    if tree is not None:
        val = rec_code(tree.left, node, val)
        if tree == node:
            nex = find_the_next_node(tree)
            return nex
        val = rec_code(tree.right, node, val)
    return val


def find_the_next_node(tree):
    if tree.right is None:
        pred = tree.parent
        while pred is not None:
            if pred.left == tree:
                return pred
            tree = pred
            pred = pred.parent
        return None
    else:
        tree = tree.right
        while tree.left is not None:
            tree = tree.left
        return tree