# Solution 2: Failing for TC 9 and 10 and the reason is 
# 	it will not consider the different string starting 
# 	from 'C' but will need to wisely choose if to take the particular 
# 	character or not.
def longestCommonSubsequence(str1, str2):
    # Write your code here.
	lcs=''
	t = len(str1)
	mxl = float('-inf')
	while(t):
		k=-1
		tmp=''
		for i in range(len(str1)-t,len(str1)):
			if str1[i] in str2[k+1:]:
				tmp += str1[i]
				k = k + str2[k+1:].index(str1[i]) + 1
		
			print(tmp, k)
		if len(tmp) > mxl:
			lcs = tmp
			mxl = len(lcs)
		t -= 1
	
	temp = []
	for ele in lcs:
		temp.append(ele)
	return temp
		


# Solution 1 : From Vdo
def longestCommonSubsequence(str1, str2):
    # Write your code here.
	lcs = [[[] for j in range(len(str2)+1)] for i in range(len(str1)+1)]
	
	for i in range(1, len(str1)+1):
		for j in range(1, len(str2)+1):
			if str1[i-1] == str2[j-1]:
				lcs[i][j] = lcs[i-1][j-1] + [str2[j-1]]
			else:
				lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1], key = len)
				
	return lcs[-1][-1]