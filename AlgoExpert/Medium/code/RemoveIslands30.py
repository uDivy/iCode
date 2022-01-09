def removeIslands(matrix):
    # Write your code here.
    visited_table = [[False] * len(row) for row in matrix]
    sol = matrix
    for row_num, row in enumerate(matrix):
        count = 0
        for col_num, ele in enumerate(row):
            queue2 = []
            if ele == 1 and not visited_table[row_num][col_num]:
                count = 1
                visited_table[row_num][col_num] = True
                queue = [[row_num, col_num]]
                queue2.append([row_num, col_num])
                while len(queue) > 0:
                    loc = queue.pop(0)
                    i = loc[0]
                    j = loc[1]
                    if j + 1 < len(row) and not visited_table[i][j + 1]:
                        visited_table[i][j + 1] = True
                        if matrix[i][j + 1] == 1:
                            queue.append([i, j + 1])
                            queue2.append([i, j + 1])
                    if i - 1 >= 0 and not visited_table[i - 1][j]:
                        visited_table[i - 1][j] = True
                        if matrix[i - 1][j] == 1:
                            queue.append([i - 1, j])
                            queue2.append([i - 1, j])
                    if j - 1 >= 0 and not visited_table[i][j - 1]:
                        visited_table[i][j - 1] = True
                        if matrix[i][j - 1] == 1:
                            queue.append([i, j - 1])
                            queue2.append([i, j - 1])
                    if i + 1 < len(matrix) and not visited_table[i + 1][j]:
                        visited_table[i + 1][j] = True
                        if matrix[i + 1][j] == 1:
                            queue.append([i + 1, j])
                            queue2.append([i + 1, j])

                # update to remove islands
                print(queue2)
                for add in queue2:
                    if check_for_borders(add[0], add[1], len(matrix), len(row)):
                        queue2.clear()
                        break
                if len(queue2) > 0:
                    for loc in queue2:
                        i = loc[0]
                        j = loc[1]
                        sol[i][j] = 0
            else:
                visited_table[row_num][col_num] = True
    return sol


def check_for_borders(row, col, sizeR, sizeC):
    if row == 0 or row == sizeR - 1:
        return True
    elif col == 0 or col == sizeC - 1:
        return True
    else:
        return False