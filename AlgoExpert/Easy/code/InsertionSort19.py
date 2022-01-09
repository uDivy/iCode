def insertionSort(array):
    # Write your code here.
    for i in range(1, len(array)):
        for j in range(0,i):
            if array[j] > array[i]:
                array[j],array[i] = array[i],array[j]
        return array