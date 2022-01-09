def searchInSortedMatrix(matrix, target):
    # Write your code here.
    row = -1
    col = -1
    found = False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                found = True
                break
            elif matrix[i][j] < target:
                continue
            else:
                break
        if found:
            row = i
            col = j
            break

    return [row, col]