def minNumberOfJumps(array):
    # Write your code here.
	jumps = [float('inf')]*len(array)
	jumps[0] = 0
	
    for i in range(1,len(array)):
		for j in range(i):
			if array[j] + j >= i:
				jumps[i] = min(jumps[i], jumps[j]+1)
				
	return jumps[-1]