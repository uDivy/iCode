def minimumWaitingTime(queries):
    # Write your code here.
	queries.sort()

	add = 0
	for curr in range(1,len(queries)):
			for t in range(0,curr):
				add += queries[t]
	return add