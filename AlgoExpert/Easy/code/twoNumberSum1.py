# ![alt text](http://AlgoExpert/Easy/files/img1.png)
def twoNumberSum(array, targetSum):
    # Write your code here.
    sum_arr = []
	
	for i,first_num in enumerate(array):
		sum_arr.append(first_num)
		second_num = targetSum - first_num
		if second_num in array[0:i] or second_num in array[i+1:len(array)]:
			sum_arr.append(second_num)
			return sum_arr
		sum_arr = []
	
	return []