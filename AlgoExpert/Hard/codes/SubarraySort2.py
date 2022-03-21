def subarraySort(array):
    # Write your code here.
	i, st, end = 0, -1, -1
	min_st = len(array)-1
	while i < len(array)-1:
		if array[i] > array[i+1]:
			end = i+1
			for st in range(0, end):
				if array[st] >= array[end]:
					break
			for sw in range(end, st, -1):
				if array[sw] < array[sw-1]:
					array[sw], array[sw-1] = array[sw-1], array[sw]
					st = sw-1
			if st < min_st:
				min_st = st
			i = 0
		print(min_st, end)
		i += 1
	return min(min_st,st), end