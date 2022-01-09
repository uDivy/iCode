# Write whatever you want here.
# Solution 1 : Mine + Video
def findClosestValueInBst(tree, target):
    # Write your code here.
    return FindClosest(tree, target, tree.value, float("inf"))


def FindClosest(tree, target, sol, val):
    if tree is None:
        return sol

    diff = abs(tree.value - target)

    if diff < val:
        val = diff
        sol = tree.value

    if target < tree.value:
        sol = FindClosest(tree.left, target, sol, val)
    elif target > tree.value:
        sol = FindClosest(tree.right, target, sol, val)
    else:
        return tree.value

    return sol


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None