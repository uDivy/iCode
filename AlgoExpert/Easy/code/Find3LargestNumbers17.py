def findThreeLargestNumbers(array):
    # Write your code here.
	temp = array[0:3]
	for val in array[3:]:
		if val > min(temp):
			i = temp.index(min(temp))
			temp[i] = val
		print(temp)
	temp.sort()
	return temp