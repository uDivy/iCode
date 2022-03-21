 # AE
 # This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
	anc1 = nodeThree
	desc1 = nodeOne


	anc2 = nodeOne
	desc2 = nodeThree
	
	return traverse(anc1, desc1, nodeTwo, False) or traverse(anc2, desc2, nodeTwo, False)
	
def traverse(start, target, middle, foundmiddle):
	if start != None and start.value == target.value and foundmiddle:
		return True
	elif start == None or start.value == target.value and not foundmiddle:
		return False
	
	if start == middle:
		foundmiddle = True
	
	if target.value < start.value:
		return traverse(start.left, target, middle, foundmiddle)
	else:
		return traverse(start.right, target, middle, foundmiddle)
	

# my
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
    if nodeTwo.value < nodeOne.value:
		if nodeOne.left == None and nodeOne.right == None:
			return False
	
		elif (nodeThree.value < nodeTwo.value or nodeThree.value >= nodeTwo.value) and nodeThree.value < nodeOne.value:
			return True
		
		else:
			return False
	
	elif nodeTwo.value >= nodeOne.value:
		if nodeOne.left == None and nodeOne.right == None:
			return False
		
		elif (nodeThree.value < nodeTwo.value or nodeThree.value >= nodeTwo.value) and nodeThree.value >= nodeOne.value:
			return True
		else:
			return False
	
	elif nodeTwo.value < nodeThree.value:
		if nodeThree.left == None and nodeThree.right == None:
			return False
		
		elif (nodeOne.value < nodeTwo.value or nodeOne.value >= nodeTwo.value) and nodeThree.value > nodeOne.value:
			return True
		else:
			return False
		
	elif nodeTwo.value >= nodeThree.value:
		if nodeThree.left == None and nodeThree.right == None:
			return False
		
		elif (nodeOne.value < nodeTwo.value or nodeOne.value >= nodeTwo.value) and nodeThree.value <= nodeOne.value:
			return True
		
		else:
			return False
		
	else:
		return False