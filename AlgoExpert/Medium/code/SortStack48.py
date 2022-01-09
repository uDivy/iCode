def sortStack(stack):
    # Write your code here.
	print(stack)
	for i in range(len(stack)-1):
		sortStackHelpers(stack)
	return stack

def sortStackHelpers(stack):
	if len(stack) == 1:
		return
	old_val = stack.pop()
	sortStackHelpers(stack)
	last_val = stack.pop()
	if last_val > old_val:
		stack.append(old_val)
		stack.append(last_val)
	else:
		stack.append(last_val)
		stack.append(old_val)
	return