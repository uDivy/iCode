# ![alt text](http://AlgoExpert/Easy/files/img3.png)
def sortedSquaredArray(array):
    # Write your code here.
	arr_sq = [i**2 for i in array]
	arr_sq.sort()
    return arr_sq