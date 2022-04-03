def maximizeExpression(array):
    # Write your code here.
	n = len(array)
	if n < 4:
		return 0
	
	tempA, tempAB, tempABC, tempABCD = [array[0]], [0, array[0]-array[1]], [0,0, array[0]-array[1] + array[2]], [0,0,0,array[0] - array[1] + array[2] - array[3]]
	for i in range(1,n):
		if i > 0:
			if array[i] >= tempA[i-1]:
				tempA.append(array[i])
			else:
				tempA.append(tempA[i-1])
		
		if i > 1: 
			if tempA[i-1] - array[i] >= tempAB[i-1]:
				tempAB.append(tempA[i-1] - array[i])
			else:
				tempAB.append(tempAB[i-1])
			
		if i > 2:
			if tempAB[i-1] + array[i] >= tempABC[i-1]:
				tempABC.append(tempAB[i-1] + array[i])
			else:
				tempABC.append(tempABC[i-1])
				
		if i > 3:
			if tempABC[i-1] - array[i] >= tempABCD[i-1]:
				tempABCD.append(tempABC[i-1] - array[i])
			else:
				tempABCD.append(tempABCD[i-1])
				
	print(tempABCD)
	return tempABCD[-1]