def longestPeak(array):
    # Write your code here.
    size = len(array)
    if size == 0:
        return size

    max_count = 0
    for i in range(size - 2):
        prev = array[i]
        peak = array[i + 1]
        down = array[i + 2]
        if prev < peak and peak > down:
            count = 3
            print(prev, peak, down)
            j = 0
            for j in reversed(range(i)):
                if prev > array[j]:
                    prev = array[j]
                    count += 1
                else:
                    break
            k = 0
            for k in range(i + 3, size):
                if down > array[k]:
                    down = array[k]
                    count += 1
                else:
                    break
            if max_count < count:
                max_count = count
            count = 0
            i = k
    return max_count