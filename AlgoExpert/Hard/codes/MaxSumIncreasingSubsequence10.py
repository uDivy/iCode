def maxSumIncreasingSubsequence(array):
    # Write your code here.
    sum_array = array[:]
	loc_array = [None]*len(array) 
	mxSumId = 0
	
	for i in range(len(array)):
		target = array[i]
		for j in range(0,i):
			curr_value = array[j]
			if curr_value < target and sum_array[j] + target >= sum_array[i]:
				sum_array[i] = sum_array[j] + target
				loc_array[i] = j
		if sum_array[i] > sum_array[mxSumId]:
			mxSumId = i
	return [sum_array[mxSumId], theSeq(array, loc_array, mxSumId)]
	
def theSeq(array, loc_array, mxSumId):
	seq = []
	while mxSumId is not None:
		seq.append(array[mxSumId])
		mxSumId = loc_array[mxSumId]
	return list(reversed(seq))
		

# Solution 2: my solution wont work for Test Case : 9
# {
#   "array": [10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50]
# }
def maxSumIncreasingSubsequence(array):
    # Write your code here.
	strictly_increasing_subsequence = build_list(array)
	total = float('-inf')
	for element in strictly_increasing_subsequence:
		plus = sum(element)
		if plus >= total:
			ans = [plus, element]
			total = plus
	return ans
	
def build_list(array):
	sol = []
	temp = []
	for i in range(len(array)):
		sol.append([array[i]])
		temp.append(array[i])
		for j in range(i+1,len(array)):
			if array[j] > max(temp):
				temp.append(array[j])
				for k in range(j+1, len(array)):
					if array[k] > max(temp):
						temp.append(array[k])
				sol.append(temp)
			print(temp)
			temp = [array[i]]
		temp = []
	return sol