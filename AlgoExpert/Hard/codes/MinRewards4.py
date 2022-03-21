def minRewards(scores):
    # Write your code here.
	size = len(scores)
    awards = [1]*size
	
	for i in range(1,size):
			if scores[i] < scores[i-1]:
				for j in range(i,0,-1):
					if scores[j] < scores[j-1]:
						awards[j-1] = max(awards[j]+1,awards[j-1])
			else:
				awards[i] =  awards[i-1] + 1
				
	return sum(awards)