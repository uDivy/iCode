from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create a graph from the flights
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))
        
        # Min-heap for BFS
        min_heap = [(0, src, 0)]  # (current_cost, current_node, stops)
        min_cost = {}  # Dictionary to track the minimum cost to reach each node with stops
        
        while min_heap:
            current_cost, current_node, stops = heapq.heappop(min_heap)
            
            # If we reach the destination and within the allowed stops
            if current_node == dst:
                return current_cost
            
            # If we still have stops left
            if stops <= k:
                for neighbor, price in graph[current_node]:
                    new_cost = current_cost + price
                    # Only consider this path if it's cheaper or we haven't reached this node with fewer stops
                    if (neighbor, stops + 1) not in min_cost or new_cost < min_cost[(neighbor, stops + 1)]:
                        min_cost[(neighbor, stops + 1)] = new_cost
                        heapq.heappush(min_heap, (new_cost, neighbor, stops + 1))
        
        return -1  # If we never reach the destination

# Test case
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1

solution = Solution()
result = solution.findCheapestPrice(4, flights, src, dst, k)
print(result)  # Output the result
        