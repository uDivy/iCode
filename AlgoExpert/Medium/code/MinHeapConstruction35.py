# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
        # basically the last parent
        fPId = (len(array)-2)//2
        # loop through all the parents
        for cId in reversed(range(fPId+1)):
            self.siftDown(cId, len(array)-1, array)
        return array

    def siftDown(self, cId, eId, heap):
        # Write your code here.
        childOne = 2*(cId) + 1
        while childOne <= eId:
            childTwo = (2*(cId) + 2) if (2*(cId) + 2) <= eId else -1
            if childTwo != -1 and heap[childTwo] < heap[childOne]:
                idS = childTwo
            else:
                idS = childOne
            if heap[idS] < heap[cId]:
                heap[cId], heap[idS] = heap[idS], heap[cId]
                cId = idS
                childOne = 2*(cId) + 1
            else:
                return

    def siftUp(self, cId, heap):
        # Write your code here.
        parent = (cId-1)//2
        while cId > 0:
            if heap[parent] < heap[cId]:
                cId = parent
                continue
            else:
                heap[cId], heap[parent] = heap[parent], heap[cId]
                cId = parent
            parent = (cId-1)//2

    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Write your code here.
        heap = self.heap
        heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
        toR = heap.pop()
        self.siftDown(0, len(heap)-1, heap)
        return toR

    def insert(self, value):
        # Write your code here.
        # we are attending the value in the last position of the array returned from build heap
        self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap)