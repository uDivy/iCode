def nodeDepths(root):
    # Write your code here.
    return call_nodeDepthsFun(root, 0, 0)


def call_nodeDepthsFun(root, total, currDep):
    if root is None:
        return total

    total += currDep

    total = call_nodeDepthsFun(root.left, total, currDep + 1)
    total = call_nodeDepthsFun(root.right, total, currDep + 1)

    return total


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
