# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []


def peek(self):
    # Write your code here.
    return self.stack[len(self.stack) - 1]


def pop(self):
    # Write your code here.
    self.minMaxStack.pop()
    return self.stack.pop()


def push(self, number):
    # Write your code here.
    nMiMa = {
        "min": number,
        "max": number
    }

    if len(self.minMaxStack):
        laMiMa = self.minMaxStack[len(self.minMaxStack) - 1]
        nMiMa["min"] = min(laMiMa["min"], number)
        nMiMa["max"] = max(laMiMa["max"], number)

    self.minMaxStack.append(nMiMa)
    self.stack.append(number)


def getMin(self):
    # Write your code here.
    laMiMa = self.minMaxStack[len(self.minMaxStack) - 1]
    return laMiMa["min"]


def getMax(self):
    # Write your code here.
    laMiMa = self.minMaxStack[len(self.minMaxStack) - 1]
    return laMiMa["max"]