def riverSizes(matrix):
    # Write your code here.
	visited_table = [[False]*len(row) for row in matrix]
	sol = []
	for row_num, row in enumerate(matrix):
		count = 0
		for col_num, ele in enumerate(row):
			if ele == 1 and not visited_table[row_num][col_num]:
				count = 1
				visited_table[row_num][col_num] = True
				queue = [[row_num, col_num]]
				while len(queue) > 0:
					print(queue)
					loc = queue.pop(0)
					i = loc[0]
					j = loc[1]
					if j + 1 < len(row) and not visited_table[i][j+1]:
						visited_table[i][j+1] = True
						if matrix[i][j+1] == 1:
							queue.append([i,j+1])
							count += 1
					if i - 1 >= 0 and not visited_table[i-1][j]:
						visited_table[i-1][j] = True
						if matrix[i-1][j] == 1:
							queue.append([i-1,j])
							count += 1
					if j - 1 >= 0 and not visited_table[i][j-1]:
						visited_table[i][j-1] = True
						if matrix[i][j-1] == 1:
							queue.append([i,j-1])
							count += 1
					if i + 1 < len(matrix) and not visited_table[i+1][j]:
						visited_table[i+1][j] = True
						if matrix[i+1][j] == 1:
							queue.append([i+1,j])
							count += 1
				print(count)
				if count > 0:
					sol.append(count)
			else:
				visited_table[row_num][col_num] = True
	return sol