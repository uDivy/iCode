def isMonotonic(array):
    # Write your code here.
    size = len(array)


    if size < 1:
        return True

    p = 0
    inc, dec = False, False
    for i in range(1, size):
        if array[p] == array[i]:
            p += 1
            continue
        elif array[p] < array[i]:
            inc = True
        else:
            dec = True
        p += 1
        print(array[p], array[i], inc, dec)

        if inc and dec:
            return False

    return True