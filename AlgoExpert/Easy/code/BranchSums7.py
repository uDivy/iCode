# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    sum_add = []
    CalculateSum(root, sum_add, 0)
    return sum_add


def CalculateSum(tree, sum_add, add):
    if tree is None:
        return

    add += tree.value
    CalculateSum(tree.left, sum_add, add)
    print(sum_add, add)
    CalculateSum(tree.right, sum_add, add)
    if tree.left is None and tree.right is None:
        print(sum_add, add)
        sum_add.append(add)

    return