def firstNonRepeatingCharacter(string):
    # Write your code here.

    size = len(string)
    i = 0
    while size > 0:
        non_rep = string[i]
        if i == size - 1:
            if string[i] not in string[0:i]:
                return i
            else:
                return -1
        elif non_rep in string[0:i] or non_rep in string[i + 1:size]:
            i += 1
        else:
            return i


    return -1
