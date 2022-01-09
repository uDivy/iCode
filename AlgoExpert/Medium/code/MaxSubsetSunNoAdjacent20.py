def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    size = len(array)


    if size == 0:
        return 0
    tot = 0
    while len(array) > 1:
        val = max(array)
        tot += val
        ind = array.index(val)
        print(val, array)
        if ind == 0:
            del array[ind:ind + 2]
        elif ind == (size - 1):
            del array[ind - 1:ind + 2]
        else:
            del array[ind - 1:ind + 2]

    if len(array) == 1:
        return tot + array[0]
    return tot