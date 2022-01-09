# Write whatever you want here.
# Solution 1 : Wrong as it cannot deal with some test cases
# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def rec_validBst(tree):
    if tree is None:
        return True
    if tree.left is not None and tree.right is not None:
        if tree.left.value > tree.value or tree.right.value < tree.value:
            return False
    elif tree.left is not None:
        if tree.left.value > tree.value:
            return False
    elif tree.right is not None:
        if tree.right.value < tree.value:
            False
    else:
        return True
    return rec_validBst(tree.left) and rec_validBst(tree.right)


def validateBst(tree):
    # Write your code here.
    return rec_validBst(tree)

# Solution 2 : Using min and max value concept: my take
# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def valid_Bst_mimax(tree, min_val, max_val):
    if tree is None:
        return True

    if min_val > tree.value or tree.value >= max_val:
        return False

    return valid_Bst_mimax(tree.left, min_val, tree.value) and valid_Bst_mimax(tree.right, tree.value, max_val)


def validateBst(tree):
    # Write your code here.
    return valid_Bst_mimax(tree, float('-inf'), float('inf'))