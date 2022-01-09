def threeNumberSort(array, order):
    # Write your code here.
	st = 0
	for ele in order:
		st = st
		end = st + 1
		while end < len(array):
			if array[st] == ele:
				st += 1
				end = st
			elif array[st] != ele and array[end] == ele:
				array[st], array[end] = array[end], array[st]
				st += 1
				end = st
			else:
				end += 1
	return array