def maxPathSum(tree):
    # Write your code here.
    _, maxSum =  possibleSol(tree)
	return maxSum
	
def possibleSol(tree):
	if tree is None:
		return (0, float("-inf"))
	
	max_left_branch_sum, max_left_sum = possibleSol(tree.left)
	max_right_branch_sum, max_right_sum = possibleSol(tree.right)
	
	max_branch_sum = max(max_left_branch_sum, max_right_branch_sum)
	max_branch_sum_root = max(max_branch_sum+tree.value, tree.value)
	max_subtree_sum = max(max_branch_sum_root, max_left_branch_sum + tree.value + max_right_branch_sum)
	current_max = max(max_left_sum, max_right_sum, max_subtree_sum)
	
	return (max_branch_sum_root, current_max)