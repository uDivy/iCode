import itertools
def fourNumberSum(array, targetSum):
    # Write your code here.
    sol = []
	for value in list(itertools.combinations(array, 4)):
		if sum(value) == targetSum:
			lst_value = list(value)
			lst_value.sort()
			sol.append(lst_value)
	sol.sort()
	return sol