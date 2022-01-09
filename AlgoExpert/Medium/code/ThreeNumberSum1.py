# Write whatever you want here.
# Solution 1 : used the combinations utility from itertools
import itertools
def threeNumberSum(array, targetSum):
    # Write your code here.
	sol = []
	print(len(list(itertools.combinations(array, 3))))
	for value in list(itertools.combinations(array, 3)):
		if sum(value) == targetSum:
			lst_value = list(value)
			lst_value.sort()
			sol.append(lst_value)
	sol.sort()
	return sol

# Solution 2 : creating my own combinations like utility
def threeNumberSum(array, targetSum):
    # Write your code here.
	size = len(array)
	temp = []
	sol = []
	for i in range(0,size-2):
		for j in range(i+1,size-1):
			for k in range(j+1,size):
				temp.append(array[i])
				temp.append(array[j])
				temp.append(array[k])
				if sum(temp) == targetSum:
					temp.sort()
					sol.append(temp)
				temp=[]
	sol.sort()
	return sol