def staircaseTraversal(height, maxSteps):
    # Write your code here.
    return staircaseTraversal_helper(height, maxSteps, {0:1, 1:1})

def staircaseTraversal_helper(height, maxSteps, memoize):
	if height in memoize:
		return memoize[height]
	
	
	totWays = 0
	for step in range(1, min(maxSteps, height)+1):
		totWays += staircaseTraversal_helper(height-step, maxSteps, memoize)
		
	memoize[height] = totWays
	
	return totWays