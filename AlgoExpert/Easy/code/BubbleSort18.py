def bubbleSort(array):
    # Write your code here.

    swaps = True
    while swaps:
        swaps = False
        for i, val in enumerate(array[0:len(array) - 1]):
            if val > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swaps = True
    return array