def kadanesAlgorithm(array):
    # Write your code here.
	curr_max_sum = 0
	max_sum = float("-inf")
	for ele in array:
		curr_max_sum += ele
		if max_sum < curr_max_sum:
			max_sum = curr_max_sum
		if curr_max_sum < 0:
			curr_max_sum = 0
	return max_sum