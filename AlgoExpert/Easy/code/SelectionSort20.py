def selectionSort(array):
    # Write your code here.

    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]
    return array