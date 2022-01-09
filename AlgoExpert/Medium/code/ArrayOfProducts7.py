def arrayOfProducts(array):
    # Write your code here.

    none = []
    prod = 1

    for index, ele in enumerate(array):
        if ele == 0:
            none.append(index)
        else:
            prod *= ele

    if len(none) > 1:
        return [0] * len(array)

    for i in range(len(array)):
        if i in none:
            array[i] = prod
            prod = 0
        else:
            array[i] = prod / array[i]

    return array