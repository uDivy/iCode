def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    checkRed = True
    checkBlue = True
    redShirtHeights.sort()
    blueShirtHeights.sort()
    for red, blue in zip(redShirtHeights, blueShirtHeights):
        if red > blue:
            checkRed = checkRed and True
            checkBlue = checkBlue and False
        elif red < blue:
            checkRed = checkRed and False
            checkBlue = checkBlue and True
        else:
            return False

    if checkRed or checkBlue:
        return True

    return False