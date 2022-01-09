def isPalindrome(string):
    # Write your code here.
    size = len(string)
    if size <= 1:
        return True

    mid = size // 2

    for i in range(0, mid):
        if string[i] != string[size - (i + 1)]:
            return False
    return True