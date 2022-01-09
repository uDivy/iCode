def spiralTraverse(array):
    # Write your code here.

    if len(array) == 0:
        return []
    if len(array) == 1:
        return array[0]
    oned = []
    sR, eR, sC, eC = 0, len(array) - 1, 0, len(array[0]) - 1

    while sR <= eR and sC <= eC:
        for c in range(sC, eC + 1):
            oned.append(array[sR][c])

        for r in range(sR + 1, eR + 1):
            oned.append(array[r][eC])

        for c in range(eC - 1, sC - 1, -1):
            if sR == eR:
                break
            oned.append(array[eR][c])

        for r in range(eR - 1, sR, -1):
            if sC == eC:
                break
            oned.append(array[r][sC])

        sR += 1
        sC += 1
        eR -= 1
        eC -= 1
    return oned