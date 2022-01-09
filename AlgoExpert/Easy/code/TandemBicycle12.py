def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    speed = 0

    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if fastest:
        redShirtSpeeds.sort(reverse=True)

    for red, blue in zip(redShirtSpeeds, blueShirtSpeeds):
        speed += max(red, blue)


    return speed
