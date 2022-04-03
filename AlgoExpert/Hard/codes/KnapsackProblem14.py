# Write whatever you want here.
# Solution 3 : tried but not working need to understand how to use DP correctly
def knapsackProblem(items, capacity):
    # Write your code here.
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]
    # sorted_list = sorted(items, key=lambda x:x[1])
	sorted_list = items[:]
	c_max_val = sorted_list[0][0]
	c_max_wt = sorted_list[0][1]
	sol = [0]*2
	
	for i in range(1,len(items)):
		tot_wt = sorted_list[i][1]
		tot_val = sorted_list[i][0]
		
		
		for j in range(0, i):
			
			tot_wt += sorted_list[j][1]
			tot_val += sorted_list[j][0]
			
			if (sorted_list[i][1] + sorted_list[j][1]) <= capacity:
				if (sorted_list[i][0] + sorted_list[j][0]) >= c_max_val:
					temp = None
					c_max_val = sorted_list[i][0] + sorted_list[j][0]
					c_max_wt = sorted_list[i][1] + sorted_list[j][1]
					temp = [j, i]
					print("a",temp,c_max_val,c_max_wt)
			
		print(tot_val, tot_wt)	
		if tot_wt <= capacity:
			
			if c_max_val <= tot_val:
				temp = []
				c_max_val = tot_val
				c_max_wt = tot_wt
				[temp.append(x) for x in range(i+1)]
				print("b",temp,c_max_val,c_max_wt)
				
		else:
			for k in range(i):
				curr_wt = tot_wt - sorted_list[k][1]
				curr_val = tot_val - sorted_list[k][0]
				if curr_wt <= capacity:
					if c_max_val <= curr_val:
						temp = []
						c_max_val = curr_val
						c_max_wt = curr_wt
						[temp.append(x) for x in range(k+1, i+1)]
						print("c",temp,c_max_val,c_max_wt)
						
		
						
			
		
	sol[0] = c_max_val
	sol[1] = temp
	return sol
			
# Solution 1 : from vdo
def knapsackProblem(items, capacity):
    # Write your code here.
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]
    row = len(items) + 1
	d_2 = [[0 for _ in range(0, capacity+1)] for _ in range(row)]
	
	for i in range(1, row):		
		it_val = items[i-1][0]
		it_wt = items[i-1][1]	
		for j in range(capacity+1):
			if it_wt <= j:
				d_2[i][j] = max((it_val+d_2[i-1][j-it_wt]),d_2[i-1][j])
			else:
				d_2[i][j] = d_2[i-1][j]
	print(d_2)			
	return [d_2[-1][-1], getTheIndex(d_2, items)]


def getTheIndex(d_2, items):
	i, j = len(d_2)-1, len(d_2[0]) - 1
	sol = []
	
	while i > 0:
		if d_2[i][j] == d_2[i-1][j]:
			i, j = i-1, j
		else:
			print(i)
			sol.append(i-1)
			i, j = i-1, j - items[i-1][1]
				
	return sol
		
		
	