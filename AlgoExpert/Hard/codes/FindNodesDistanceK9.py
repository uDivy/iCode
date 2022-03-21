# AE
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    # Write your code here.
	yourParent = {} # mapping each value to the parent
	kNeighbour = [] # node at distance k
	
	find_yourParent(tree, yourParent)
	
	if tree.value == target:
		tarAd = tree
	else:
		tarAd = yourParent[target].left if yourParent[target].left is not None and yourParent[target].left.value == target else yourParent[target].right
	
	# create a bfs function which will search till we find all the node in region distant at k
	return bfs(tarAd, yourParent, k, kNeighbour)

def find_yourParent(tree, yourParent, parent=None):
	if tree is not None:
		yourParent[tree.value] = parent
		find_yourParent(tree.left, yourParent, parent=tree)
		find_yourParent(tree.right, yourParent, parent=tree)
		
def bfs(tarAd, yourParent, k, kNeighbour):	
	queue = []
	queue.append((tarAd, 0)) # the node and its distance from target
	seen = set([tarAd.value]) # to know all the nodes I already visited
	while len(queue):
		myAd, distFromTarget = queue.pop(0)
		seen.add(myAd.value)
		myNei = [myAd.left, myAd.right, yourParent[myAd.value]]
		
		if distFromTarget == k:
			kNeighbour = [entry.value for entry, _ in queue] + [myAd.value]
			break
		
		for entry in myNei:
			if entry is not None and entry.value not in seen:
				queue.append((entry, distFromTarget+1)) 
				
	return kNeighbour

#Solution 2 : My algo, not worked for target whoses depth is more than k, like leaf node, but have corresponded siblings and grandparents with k distance, Test Case 6
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    # Write your code here.
	root = tree
	search_list = []
	tarAd = root
	find = []
	
	if tree.value == target:
		target_side = None
		target_gap = 0
		search_under(tarAd,0,k,search_list)
		return search_list
	else:
		if find_the_target_side(tree.left, target, False):
			target_side = "L"
		else:
			target_side = "R"
		
		if target_side == "L":
			target_gap, tarAd = find_the_dist_between_root_target(tree.left, target, 1, 0, None)
		else:
			target_gap, tarAd = find_the_dist_between_root_target(tree.right, target, 1, 0, None)
		
		print(target_side, target_gap, tarAd)
	
	search_under(tarAd,0,k,search_list)
	# print(search_list)
	
	if k == target_gap:
		search_list.append(root.value)
		return search_list
	elif k < target_gap:
		print(k," is mysterious")
		return search_list
	else:
		k = k - target_gap
		if target_side == 'L':
			search_under(root.right,1,k,search_list)
		else:
			search_under(root.left,1,k,search_list)
		return search_list

def find_the_target_side(tree, target,side):
	if tree is None:
		return side
	
	if tree.value == target:
		side = True
	
	side = find_the_target_side(tree.left, target,side)
	side = find_the_target_side(tree.right, target,side)
	
	return side
	
def find_the_dist_between_root_target(tree, target, count, ans, tarAd):
	if tree is None:
		return ans, tarAd
	
	if tree.value == target:
		ans, tarAd = count, tree
		
	ans, tarAd = find_the_dist_between_root_target(tree.left, target, count+1, ans, tarAd)
	ans, tarAd = find_the_dist_between_root_target(tree.right, target, count+1, ans, tarAd)
	
	return ans, tarAd

def search_under(tree, count, k, search_list):
	if tree is None:
		return 
	
	if count == k:
		search_list.append(tree.value)
		
	search_under(tree.left, count+1, k, search_list)
	search_under(tree.right, count+1, k, search_list)	
	
def find_the_target_parent(tree, target, parent):
	if tree is None:
		return parent
	
	if tree.left == target or tree.right == target:
		parent = tree
		
	parent = find_the_target_parent(tree.left, target, parent)
	parent = find_the_target_parent(tree.right, target, parent)
	
	return parent