# Write whatever you want here.
# Solution 1 : Non Recursive
# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        temp = BST(value)
        while self is not None:
            if value >= self.value:
                if self.right is None:
                    self.right = temp
                    break
                self = self.right
            elif value < self.value:
                if self.left is None:
                    self.left = temp
                    break
                self = self.left

        return self

    def contains(self, value):
        # Write your code here.
        while self is not None:
            if value > self.value:
                self = self.right
            elif value < self.value:
                self = self.left
            else:
                return True
        return False

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        root = self
        prev = root
        while self is not None:
            if value > self.value:
                prev = self
                self = self.right
            elif value < self.value:
                prev = self
                self = self.left
            else:
                break
        to_be_delete = self
        if self.right is not None:
            prev = self
            self = self.right
            while self.left is not None:
                prev = self
                self = self.left
            to_be_delete.value = self.value
            if prev.right == self:
                prev.right = self.right
            elif self.right is not None:
                prev.left = self.right
            else:
                prev.left = None
        elif self.left is not None:
            prev = self
            self = self.left
            while self.right is not None:
                prev = self
                self = self.right
            to_be_delete.value = self.value
            if prev.left == self:
                prev.left = self.left
            elif self.left is not None:
                prev.right = self.left
            else:
                prev.right = None
        else:
            if prev.left == self:
                prev.left = None
            else:
                prev.right = None

        return self

# Solution 2 : Recursive
# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        temp = BST(value)
        if value >= self.value:
            if self.right is None:
                self.right = temp
            else:
                self = self.right
                self.insert(value)
        elif value < self.value:
            if self.left is None:
                self.left = temp
            else:
                self = self.left
                self.insert(value)

        return self

    def contains(self, value):
        # Write your code here.
        if value > self.value:
            if self.right is not None:
                self = self.right
                return self.contains(value)
            else:
                return False
        elif value < self.value:
            if self.left is not None:
                self = self.left
                return self.contains(value)
            else:
                return False
        else:
            return True

    def remove_rec(self, prev, value):

        if value > self.value:
            prev = self
            self = self.right

        elif value < self.value:
            prev = self
            self = self.left

        else:
            to_be_delete = self
            if self.right is not None:
                prev = self
                self = self.right
                while self.left is not None:
                    prev = self
                    self = self.left
                to_be_delete.value = self.value
                if prev.right == self:
                    prev.right = self.right
                elif self.right is not None:
                    prev.left = self.right
                else:
                    prev.left = None
            elif self.left is not None:
                prev = self
                self = self.left
                while self.right is not None:
                    prev = self
                    self = self.right
                to_be_delete.value = self.value
                if prev.left == self:
                    prev.left = self.left
                elif self.left is not None:
                    prev.right = self.left
                else:
                    prev.right = None
            else:
                if prev.left == self:
                    prev.left = None
                else:
                    prev.right = None

            return self

        return self.remove_rec(prev, value)

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self.remove_rec(self, value)


