def minimumPassesOfMatrix(matrix):
    # Write your code here.
    step = 0
    queue_one, queue_two = [], []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value > 0:
                queue_one.append([i, j])

    while len(queue_one) > 0:
        loc = queue_one.pop(0)
        i = loc[0]
        j = loc[1]
        change = check_the_neighbours(matrix, i, j)

        if len(change) > 0:
            for val in change:
                queue_two.append(val)
        print(queue_one, queue_two)
        if len(queue_one) == 0:
            step += 1
            queue_one = queue_two.copy()
            queue_two = []

    test = check_for_negative(matrix)
    if test:
        return step - 1
    else:
        return -1


def check_the_neighbours(matrix, i, j):
    up, right, down, left = float("inf"), float("inf"), float("inf"), float("inf")
    if (j + 1) < len(matrix[i]):
        right = matrix[i][j + 1]
    if i - 1 >= 0:
        up = matrix[i - 1][j]
    if j - 1 >= 0:
        left = matrix[i][j - 1]
    if i + 1 < len(matrix):
        down = matrix[i + 1][j]
    change = []
    if up < 0:
        change.append([i - 1, j])
        matrix[i - 1][j] = -1 * matrix[i - 1][j]
    if right < 0:
        change.append([i, j + 1])
        matrix[i][j + 1] = -1 * matrix[i][j + 1]
    if down < 0:
        change.append([i + 1, j])
        matrix[i + 1][j] = -1 * matrix[i + 1][j]
    if left < 0:
        change.append([i, j - 1])
        matrix[i][j - 1] = -1 * matrix[i][j - 1]

    return change


def check_for_negative(matrix):
    for row in matrix:
        for value in row:
            if value < 0:
                return False
    return True