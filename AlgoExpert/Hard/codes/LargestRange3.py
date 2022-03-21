def largestRange(array):
    # Write your code here.
	array.sort()
	size = len(array)
	
	rang = 0
	st, end = array[0], array[size-1]
	for i in range(len(array)):
		stp = array[i]
		endp = stp + len(array[i:]) - 1	
		for val in range(stp+1, endp+1):
			if val in array:
				endp = val
				if rang < (endp - stp):
					rang = endp - stp
					st = stp
					end = endp
				continue
			else:
				break
	return [st, end]