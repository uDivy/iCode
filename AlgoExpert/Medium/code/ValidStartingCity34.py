# Write whatever you want here.
# Solution 1 : Brute Force O(n^2)
def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    for st in range(0,len(distances)):
		rem_fuel = fuel[st]
		journey = distances[st]
		can_go = rem_fuel*mpg
		if journey > can_go:
			continue
		end = st
		dest = st + 1
		while dest != end:
			dest = (dest)%len(distances)
			rem_fuel = fuel[dest] + (can_go-journey)/mpg
			can_go = rem_fuel*mpg
			journey = distances[dest]
			if journey > can_go or dest == end:
				break
			dest += 1
		if dest == end:
			return end

    return -1

# Solution 2 : Greedy Algorithm
