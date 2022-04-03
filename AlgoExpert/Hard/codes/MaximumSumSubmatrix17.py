def maximumSumSubmatrix(matrix, size):
    # Write your code here.
	if size == 0:
		return -1
	
	bigNum = float("-inf")
    sumMatrix = createTheSumMatrix(matrix)
	print(sumMatrix)
	
	for i in range(0,len(sumMatrix)+1-size):
		for j in range(size-1, len(sumMatrix[i])):
			if i == 0 and j == size-1:
				if bigNum <= sumMatrix[(size+i)-1][j]:
					bigNum = sumMatrix[(size+i)-1][j]
			elif i == 0:
				#topborder
				if bigNum <= (sumMatrix[size-1][j] - sumMatrix[size-1][j-size]):
					bigNum = (sumMatrix[size-1][j] - sumMatrix[size-1][j-size])
			elif i != 0 and j == size-1:
				#leftborder
				if bigNum <= (sumMatrix[(size+i)-1][j] - sumMatrix[i-1][j]):
					bigNum = (sumMatrix[(size+i)-1][j] - sumMatrix[i-1][j])
			else:
				#otherwise
				if bigNum <= (sumMatrix[(size+i)-1][j] - sumMatrix[(size+i)-1][j-size] - sumMatrix[i-1][j] + sumMatrix[i-1][j-size]):
					bigNum = (sumMatrix[(size+i)-1][j] - sumMatrix[(size+i)-1][j-size] - sumMatrix[i-1][j] + sumMatrix[i-1][j-size])
			
			print(i, j, bigNum)
				
	return bigNum	
				
			
	
	
def createTheSumMatrix(matrix):
	sumMatrix = [[0 for _ in range(len(i))] for i in matrix]
	
	tot = 0
	j = 0
	for firstRowValue in matrix[0]:
		tot += firstRowValue
		sumMatrix[0][j] = tot
		j += 1
	
	tot = 0
	i = 0
	for firstColValue in matrix:
		tot += firstColValue[0]
		sumMatrix[i][0] = tot
		i += 1	
		
	for row in range(1, len(matrix)):
		for col in range(1, len(matrix[row])):
			sumMatrix[row][col] = matrix[row][col] + sumMatrix[row-1][col] + sumMatrix[row][col-1] - sumMatrix[row-1][col-1]
			
	return sumMatrix