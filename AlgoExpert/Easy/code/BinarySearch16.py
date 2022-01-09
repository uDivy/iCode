# Write whatever you want here.
# Solution 1 : Wrote the code but some test cases are not working
import math


def binarySearch(array, target):
    # Write your code here.
    mid = math.floor(len(array) / 2)
    if array[mid] == target:
        return
    elif target < array[mid]:
        binarySearch(array[0:mid], target)
    elif target > array[mid]:
        binarySearch(array[mid:len(array)], target)
    else:
        return -1

    return array.index(target)

# Solution 2 : Watched the video and modify the code from Solution 1
def binarySearch(array, target):
    # Write your code here.
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    if (left - right) > 0:
        return -1

    mid = (left + right) // 2

    if array[mid] == target:
        return mid
    elif target < array[mid]:
        sol = binarySearchHelper(array, target, left, mid - 1)
    elif target > array[mid]:
        sol = binarySearchHelper(array, target, mid + 1, right)

    return sol