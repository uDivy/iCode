# Write whatever you want here.
# Solution 1: Tried the Brute Force approach, but it is getting complicated
# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    # Write your code here.
    pos = 0
    return RecProductSum(array, 1, len(array), 0, pos, array[pos])


def RecProductSum(array, depth, l, total, pos, value):
    if l == 0:
        return total

    print(total, value, depth)

    if isinstance(value, (int)):
        total += depth * value
    else:
        temp = 0
        for ele in value:
            if isinstance(ele, (int)):
                total = RecProductSum(array, depth * (depth + 1), l, 0, pos, ele)
            else:
                total = RecProductSum(array, depth * (depth + 1), l, total, pos, ele)

        total = RecProductSum(array, depth * (depth + 1), l, total, pos, temp)

    total = RecProductSum(array, 1, l - 1, total, pos + 1, array[pos + 1])

    return total


# SOlution 2: Referring their solution
# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    # Write your code here.
    return RecProductSum(array, 1)


def RecProductSum(array, multiplier=1):
    temp = 0

    for value in array:

        if type(value) is list:
            value = RecProductSum(value, multiplier + 1)

        temp += value

    return multiplier * temp