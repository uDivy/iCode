# Write whatever you want here.
# Solution1 : Time Complexity O(n^m)
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    curr_diff = 999999
    for a1 in arrayOne:
        for a2 in arrayTwo:
            if a1 > 0 and a2 < 0:
                obt_diff = (a1 + abs(a2))
            elif a1 < 0 and a2 > 0:
                obt_diff = (abs(a1) + a2)
            else:
                obt_diff = (abs(abs(a1) - abs(a2)))

            if curr_diff > obt_diff:
                temp = []
                curr_diff = obt_diff
                temp.append(a1)
                temp.append(a2)

    return temp

# Solution2 : Time Complexity O(mlogm + nlogn) due to sort function, from the AE solution
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()

    size1, size2 = len(arrayOne), len(arrayTwo)
    i, j = 0, 0
    sm = float("inf")
    curr = float("inf")
    sol = []

    while i < size1 and j < size2:
        a1 = arrayOne[i]
        a2 = arrayTwo[j]

        if a1 < a2:
            curr = a2 - a1
            i += 1
        elif a2 < a1:
            curr = a1 - a2
            j += 1
        else:
            return [a1, a2]

        if sm > curr:
            sm = curr
            sol = [a1, a2]

    return sol