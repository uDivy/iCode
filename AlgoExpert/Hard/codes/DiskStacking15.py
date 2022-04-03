def diskStacking(disks):
    # Write your code here.
	sorted_disks_h = sorted(disks, key = lambda x:x[2])
    heights = [item[2] for item in sorted_disks_h]
	seq = [None]*len(disks)
	sol = []
	maxId = 0
	print(sorted_disks_h)
	for i in range(1, len(disks)):
		for j in range(0, i):
			if sorted_disks_h[j][0] < sorted_disks_h[i][0] and sorted_disks_h[j][1] < sorted_disks_h[i][1] and sorted_disks_h[j][2] < sorted_disks_h[i][2]:
				if heights[i] <= sorted_disks_h[i][2] + heights[j]:
					heights[i] = sorted_disks_h[i][2] + heights[j]
					seq[i] = j
				
		if heights[i] >= heights[maxId]:
			maxId = i
					
	return buildSeq(sorted_disks_h, seq, maxId)

def buildSeq(array, seq, curId):
	sequence = []
	while curId is not None:
		sequence.append(array[curId])
		curId = seq[curId]
		
	return list(reversed(sequence))