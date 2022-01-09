def getNthFib(n):
    # Write your code here.

    num1, num2 = 0, 1
    c = 0

    if n == 1:
        return num1
    if n == 2:
        return num2

    for i in range(2, n):
        c = num1 + num2
        num1, num2 = num2, c

    return c