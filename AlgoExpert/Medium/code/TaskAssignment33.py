def taskAssignment(k, tasks):
    # Write your code here.
    orch = []
    # for i in range(0,k):
    # 	orch.append([tasks_save.index(tasks[i],i),tasks_save.index(tasks[(2*k)-(i+1)])])

    for i in range(0, k):
        mi = tasks.index(min(v for v in tasks if v >= 0))
        ma = tasks.index(max(v for v in tasks if v >= 0))
        orch.append([mi, ma])
        tasks[mi], tasks[ma] = -1, -1
    print(orch)
    return orch