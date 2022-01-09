def sunsetViews(buildings, direction):
    # Write your code here.
    enjoy = []
    for i,h in enumerate(buildings):
        if direction == "EAST":
            if i == len(buildings)-1:
                enjoy.append(i)
            else:
                is_taller = max(buildings[i+1:])
                if h > is_taller:
                    enjoy.append(i)
        else:
            if i == 0:
                enjoy.append(i)
            else:
                is_taller = max(buildings[0:i])
                if h > is_taller:
                    enjoy.append(i)

    return enjoy
