def powerset(array):
    # Write your code here.
    powerset = []
    powHelper(array, [], powerset)
    return powerset


def powHelper(array, cur, powerset):
    powerset.append(cur)
    if not array:
        return
    else:
        for l in range(len(array)):
            newArray = array[l + 1:]
            newpowerset = cur + [array[l]]
            powHelper(newArray, newpowerset, powerset)