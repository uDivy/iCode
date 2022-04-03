def numbersInPi(pi, numbers):
    # Write your code here.
    numbersTable = {number:True for number in numbers}
	minSpaces = getminSpaces(pi, numbersTable, {}, 0)
	return -1 if minSpaces == float('inf') else minSpaces

def getminSpaces(pi, numbersTable, cache, idx):
	if idx == len(pi):
		return -1
	if idx in cache:
		return cache[idx]
	
	minSpaces = float("inf")
	
	for i in range(idx, len(pi)):
		prefix = pi[idx:i+1]
		if prefix in numbersTable:
			minSpacesInSuffix = getminSpaces(pi, numbersTable, cache, i+1)
			print(idx, cache)
			minSpaces = min(minSpaces, minSpacesInSuffix+1)
			
	cache[idx] = minSpaces
	
	return minSpaces