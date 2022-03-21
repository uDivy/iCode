def zigzagTraverse(array):
    # Write your code here.
    ht, wd = len(array)-1, len(array[0]) - 1
	traversal = []
	row, col = 0, 0
	goingDown = True
	
	while not isOutofBounds(row, col, ht, wd):
		traversal.append(array[row][col])
		
		if goingDown:
			if col == 0 or row == ht:
				goingDown = False
				if row == ht:
					col += 1
				else:
					row += 1
			else:
				row += 1
				col -= 1
		else:
			if col == wd or row == 0:
				goingDown = True
				if col == wd:
					row += 1
				else:
					col += 1
			else:
				row -= 1
				col += 1
				
	return (traversal)
	
def isOutofBounds(row, col, ht, wd):
	return row < 0 or row > ht or col < 0 or col > wd