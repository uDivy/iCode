def dijkstrasAlgorithm(start, edges):
    # Write your code here.
    totNodes = len(edges)
	minDis = [float("inf") for _ in range(totNodes)]
	minDis[start] = 0
	
	seen = set()
	
	while len(seen) != totNodes:
		vertex, curMinDis = getVerCurMin(minDis, seen)
	
		if curMinDis == float("inf"):
			break

		seen.add(vertex)

		for edge in edges[vertex]:
			destination, distToDestination = edge

			if destination in seen:
				continue

			newPathDis = curMinDis + distToDestination
			moveWithThisWay = minDis[destination]
			if newPathDis < moveWithThisWay:
				minDis[destination] = newPathDis
			
	return list(map(lambda x: -1 if x == float("inf") else x, minDis))
		
def getVerCurMin(Distances, seen):
	curMinDis = float("inf")
	vertex = -1
	
	for verIdx, dis in enumerate(Distances):
		if verIdx in seen:
			continue
			
		if dis <= curMinDis:
			vertex = verIdx
			curMinDis = dis
			
	return vertex, curMinDis