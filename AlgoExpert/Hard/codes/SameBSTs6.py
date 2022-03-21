# Solution 1 AE
def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    if len(arrayOne) != len(arrayTwo):
		return False
	
	if len(arrayOne) == 0 and len(arrayTwo) == 0:
		return True
	
	if arrayOne[0] != arrayTwo[0]:
		return False
	
	leftOne = getSmaller(arrayOne)
	leftTwo = getSmaller(arrayTwo)
	
	rightOne = getBiggerOrEqual(arrayOne)
	rightTwo = getBiggerOrEqual(arrayTwo)
	
	return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)

def getSmaller(array):
	smaller = []
	for i in range(1, len(array)):
		if array[i] < array[0]:
			smaller.append(array[i])
	return smaller
	
def getBiggerOrEqual(array):
	bigger = []
	for i in range(1, len(array)):
		if array[i] >= array[0]:
			bigger.append(array[i])
	return bigger

# Solution 2 : iCode
def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    if arrayOne[0] != arrayTwo[0] or len(arrayOne) != len(arrayTwo):
		return False
	else:
		rootM = arrayOne[0]
		rootR, rootL = rootM, rootM
		for i in range(1,len(arrayOne)):
			val = arrayOne[i]
			for j in range(1,len(arrayTwo)):
				tmp = []
				for k in range(i):
					if arrayOne[k] >= rootM:
						tmp.append(arrayOne[k])
						rootR = max(tmp)
				tmp = []
				for k in range(i):
					if arrayOne[k] < rootM:
						tmp.append(arrayOne[k])
						rootL = max(tmp)
				print(val, rootR, rootL, arrayTwo[j])
				if arrayTwo[j] > val:
					return False
				elif arrayTwo[j] < val:
					if rootM <= val and arrayTwo[j] >= rootM:
						if arrayTwo[j] >= rootR and val >= rootR:
							if arrayTwo[j] > val:
								return False
							else:
								continue
						else:
							if arrayTwo[j] < val and val < rootR:
								tmp = []
								for k in range(i-2,0,-1):
									if arrayOne[k] >= rootM:
										tmp.append(arrayOne[k])
										let = max(tmp)
								if arrayTwo[j] >= let:
									return False
								elif  val < let and arrayTwo[j] < val:
									return False
								else:
									continue
							else:
								continue
							
					else:
						if arrayTwo[j] < rootL and val < rootL:
							if arrayTwo[j] < val:
								return False
							else:
								continue
						else:
							if arrayTwo[j] > val:
								return False
							else:
								continue
				elif arrayTwo[j] == val:
					del arrayTwo[j]
					break
				else:
					return False
		return True
