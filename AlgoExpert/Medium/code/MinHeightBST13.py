def minHeightBst(array):
    array.sort()
    size = len(array)
    val = array[size // 2]
    root = BST(val)
    return make_it_binary(array, 0, size, root)


def make_it_binary(array, start, end, root):
    mid = (start + end) // 2
    if start < end:
        if root.value != array[mid]:
            root.insert(array[mid])
        make_it_binary(array, start, mid, root)
        make_it_binary(array, mid + 1, end, root)
    return root


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
