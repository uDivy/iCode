def hasSingleCycle(array):
    # Write your code here.
	size = len(array)
	total = (size)*(size-1)//2
	val = array[0]
	landed_on = 0
	temp = []

    for i in range(0,size):
		landed_on = (landed_on+(size+val))%size
		val = array[landed_on]
		temp.append(landed_on)
	if temp[size-1]==0 and sum(temp[0:size-1]) == total:
		return True
	return False