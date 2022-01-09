# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    d1 = find_depth_of_descendant(topAncestor, descendantOne, 0)
	d2 = find_depth_of_descendant(topAncestor, descendantTwo, 0)
	if d1 > d2:
		for i in range(0,(d1-d2)):
			descendantOne = descendantOne.ancestor
	elif d2 > d1:
		for i in range(0,(d2-d1)):
			descendantTwo = descendantTwo.ancestor
	while descendantOne != descendantTwo:
		descendantOne = descendantOne.ancestor
		descendantTwo = descendantTwo.ancestor
	return descendantOne

def find_depth_of_descendant(topAncestor, descendant, d):
	if topAncestor.name is descendant.name:
		return d
	d = find_depth_of_descendant(topAncestor, descendant.ancestor, d+1)
	return d