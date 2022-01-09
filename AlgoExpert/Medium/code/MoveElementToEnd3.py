def moveElementToEnd(array, toMove):
    # Write your code here.
	size = len(array)
	i = 0
	j = size - 1
	while i < j:
		if array[i] != toMove:
			i += 1
		elif array[j] == toMove:
			j -= 1
		else:
			array[i], array[j] = array[j], array[i]
	return array