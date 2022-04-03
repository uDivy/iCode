def waterArea(heights):
    # Write your code here.
    sol, curr_h, value_till, to_add = 0, 0, -1, 0
	for i in range(len(heights)-1):
		print(curr_h, to_add, value_till, sol)
		
		if heights[i] == 0:
			sol = sol + curr_h + to_add
			to_add = 0
		else:
			if i >= value_till:
				curr_h = min(heights[i], max(heights[i+1:]))
				value_till = 1 + i + heights[i+1:].index(max(heights[i+1:]))
			else:
				to_add += abs((curr_h-heights[i]))
		
	if sol == 0:
		return to_add
	return sol