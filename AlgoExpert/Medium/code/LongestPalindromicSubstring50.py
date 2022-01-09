def longestPalindromicSubstring(string):
    # Write your code here.s
    pal = ''
    old_len = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            check = isPal(string[i:j + 1])
            print(check, string[i:j + 1])
            if check:
                curr_len = len(string[i:j + 1])
                if old_len < curr_len:
                    pal = string[i:j + 1]
                    old_len = curr_len

    return pal


def isPal(string):
    size = len(string)
    if size == 1:
        return True
    else:
        st = 0
        end = len(string) - 1
        while st < end:
            if string[st] != string[end]:
                return False
            st += 1
            end -= 1
    return True