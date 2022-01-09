# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    obj = cal_height_diamter(tree)
    return obj.diameter


class TreeIn:
    def __init__(self, height, diameter):
        self.height = height
        self.diameter = diameter


def getTreeIn(TreeLObj, TreeRObj):
    lSH = TreeLObj.height
    rSH = TreeRObj.height
    mH = 1 + max(lSH, rSH)
    cD = lSH + rSH
    mD = max(TreeLObj.diameter, TreeRObj.diameter, cD)
    return TreeIn(mH, mD)


def cal_height_diamter(tree):
    if tree is None:
        return TreeIn(0, 0)

    return getTreeIn(cal_height_diamter(tree.left), cal_height_diamter(tree.right))