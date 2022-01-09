def mergeOverlappingIntervals(intervals):
    # Write your code here.
    i = 0
    while i < len(intervals):
        v = intervals[i]
        for j, val in enumerate(intervals):
            if i == j:
                continue
            if v[0] <= val[0] <= v[1] or val[0] <= v[0] <= val[1]:
                intervals[i] = [min(v[0], val[0]), max(v[1], val[1])]
                intervals.remove(val)
                i = -1
                break
        i += 1

    return intervals