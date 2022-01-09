# Write whatever you want here.
# Solution 1: my solution ; not generalized
def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    # Write your code here.
    if len(denoms) == 1:
        if n % denoms[0] == 0:
            return 1
        else:
            return -1

    sol = []
    denoms.sort()


    for ind, d in enumerate(denoms):
        change = [0] * (n + 1)
        for value in range(1, n + 1):
            if ind == 0:
                if (value % d) == 0:
                    change[value] = value // d
            elif value < d:
                change[value] = sol[ind - 1][value]
            elif value == d:
                change[value] = 1
            else:
                if change[value - d] == 0:
                    change[value] = sol[ind - 1][value]
                else:
                    change[value] = min(change[value - d] + 1, sol[ind - 1][value])
        sol.append(change)
        print(sol)
    if (sol[len(sol) - 1][len(sol[-1]) - 1]) == 0 and n != 0:
        return -1

    return (sol[len(sol) - 1][len(sol[-1]) - 1])