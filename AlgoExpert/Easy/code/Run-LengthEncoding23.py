# Write whatever you want here.
# Solution 1 : O(n^2)
def runLengthEncoding(string):
    # Write your code here.
    size = len(string)
    i = 0
    temp = ''
    while i < size:
        char = string[i]
        counter = 0
        for letter in string[i:]:
            if letter != char:
                break
            counter += 1
            i += 1
        if counter > 9:
            temp += (counter // 9) * (str(9) + char) + str(counter % 9) + char
        else:
            temp += str(counter) + char

    return temp

# Solution 2 : O(n)
def runLengthEncoding(string):
    # Write your code here.
    size = len(string)
    i = 0
    temp = ''
    char = string[0]
    counter = 1
    for i in range(1, size):
        if string[i] != char:
            if counter > 9:
                temp += (counter // 9) * (str(9) + char) + str(counter % 9) + char
            else:
                temp += str(counter) + char
            char = string[i]
            counter = 0
        counter += 1

    if counter > 9:
        temp += (counter // 9) * (str(9) + char) + str(counter % 9) + char
    else:
        temp += str(counter) + char
    return temp