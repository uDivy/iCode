# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

        def insert(self, value):
            if self.value > value:
                if self.left is not None:
                    return self.left.insert(value)
                self.left = BST(value)

            elif self.value <= value:
                if self.right is not None:
                    return self.right.insert(value)
                self.right = BST(value)

            return self


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    root = BST(preOrderTraversalValues[0])


    for val in preOrderTraversalValues[1:]:
        root.insert(val)

    return root




