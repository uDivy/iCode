def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    if len(denoms) == 1:
        if n % denoms[0] == 0:
            return 1
        else:
            return 0

    sol = []


    for ind, d in enumerate(denoms):
        change = [0] * (n + 1)
        change[0] = 1
        for value in range(1, n + 1):
            if ind == 0:
                if (value % d) == 0:
                    change[value] += 1
            elif value < d:
                change[value] = sol[ind - 1][value]
            elif value == d:
                change[value] = sol[ind - 1][value] + 1
            else:
                change[value] = sol[ind - 1][value] + change[value - d]
        sol.append(change)

    return (sol[len(sol) - 1][len(sol[-1]) - 1])