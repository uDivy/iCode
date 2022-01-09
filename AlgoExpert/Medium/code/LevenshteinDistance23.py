def levenshteinDistance(str1, str2):
    # Write your code here.
	size1, size2 = len(str1), len(str2)
	mat = []
	for i in range(0,size1+1):
		line = [0]*(size2+1)
		for j in range(0,size2+1):
			if i == 0 and j == 0:
				continue
			elif i == 0:
				line[j] = line[j-1] + 1
			elif j == 0:
				line[j] = mat[i-1][0] + 1
			else:
				if str1[i-1] == str2[j-1]:
					line[j] = mat[i-1][j-1]
				else:
					line[j] = min(line[j-1],mat[i-1][j],mat[i-1][j-1])+1
		mat.append(line)
	return mat[size1][size2]