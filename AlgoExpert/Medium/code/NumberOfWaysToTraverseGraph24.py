def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.

	sol = []

	for i in range(0, height):
		count = [0]*width
		for j in range(0,width):
			if i == 0 and j == 0:
				continue
			elif i == 0 or j == 0:
				count[j] = 1
			else:
				count[j] = count[j-1] + sol[i-1][j]
		sol.append(count)

	return sol[height-1][width-1]