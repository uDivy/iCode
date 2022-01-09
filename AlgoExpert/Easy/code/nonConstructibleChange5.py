# ![alt text](http://AlgoExpert/Easy/files/img5.png)
# Write whatever you want here.
# This is to solve through recursion then DP.
# Solution 1 : Failed Attempt
def nonConstructibleChange(coins):
    # Write your code here.
	if coins == []:
		return 1
	
	coins.sort()
	total = sum(coins)
	size = len(coins)
	
	for value in range(coins[0],total):
		if value in coins:
			continue
		save = value
		for i in range(0,size-1):
			value = save 
			find = False
			for j,option in enumerate(coins[i:size]):  
				if option >= value:
					print("option {} value {}".format(option,value))
					break
				print("j {} option {} value {}".format(j+i,option,value))
				print(coins[j+i:])
				if abs(value - option) in coins[j+i:]:
					find = True
					break
				value = value - option
			if find:
				print("="*50)
				break
		print(find)
		if not find:
			return save
			
	return total + 1


# Solution 2 : From Video
def nonConstructibleChange(coins):
    # Write your code here.if coins == []:
	if coins == []:
		return 1
	
	coins.sort()
	change = 0
	
	for coin in coins:
		if coin > change+1:
			return change + 1
		change += coin
		
	return change + 1