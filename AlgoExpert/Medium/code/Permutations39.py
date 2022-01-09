def getPermutations(array):
    # Write your code here.
    permutations = []


if array == []:
    return permutations

getPermHelper(array, [], permutations)
return permutations


def getPermHelper(array, cur_permutations, permutations):
    if not len(array):
        permutations.append(cur_permutations)

    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1:]
            newPermutations = cur_permutations + [array[i]]
            getPermHelper(newArray, newPermutations, permutations)