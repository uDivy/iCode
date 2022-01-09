def cycleInGraph(edges):
    # Write your code here.
    cycle = False


    for ind, adjL in enumerate(edges):

        if len(adjL) == 0:
            continue

        route = [False for i in range(0, len(edges))]
        route[ind] = True
        queue = [adjL]

        while len(queue) > 0:

            loc = queue.pop(0)
            print(loc)
            for node in loc:
                if route[node] == True:
                    cycle = True
                    break
                else:
                    if len(edges[node]) > 0:
                        route[node] = True
                        queue.append(edges[node])
                        break

            if cycle:
                break

        if cycle:
            break

    return cycle