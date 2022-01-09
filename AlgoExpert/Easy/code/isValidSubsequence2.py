# ![alt text](http://AlgoExpert/Easy/files/img2.png)
def isValidSubsequence(array, sequence):
    # Write your code here.
	old_pos = -1
    for element in sequence:
		try:
			position = array.index(element, old_pos+1)
			old_pos = position
		except ValueError:
			return False
		
	return True