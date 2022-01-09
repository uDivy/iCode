def firstDuplicateValue(array):
    # Write your code here.

    i = 0
    j = len(array)
    while i < j:
        if array[i] in array[i + 1:j]:
            j = array.index(array[i], i + 1, j)

        i += 1

    if j == len(array):
        return -1
    return array[j]