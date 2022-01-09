def phoneNumberMnemonics(phoneNumber):
    # Write your code here.

    mnemonics = []
    cur = ["0"] * len(phoneNumber)
    pnum_helper(0, phoneNumber, cur, mnemonics)

    return mnemonics


def pnum_helper(idx, phNum, cur, mnemonics):
    if idx == len(phNum):
        mnem = "".join(cur)
        mnemonics.append(mnem)
    else:
        for num in phNum[idx]:
            for key in keypad[num]:
                cur[idx] = key
                pnum_helper(idx + 1, phNum, cur, mnemonics)


keypad = {
    '0': ['0'],
    '1': ['1'],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}