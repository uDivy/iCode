class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        import heapq
        
        # Max-heap to keep track of the bricks used at each step (invert the values for max-heap)
        max_heap = []
        
        for i in range(len(heights) - 1):
            # Calculate the difference in height
            diff = heights[i + 1] - heights[i]
            
            if diff > 0:
                # Use bricks for the current height difference (invert diff for max-heap)
                heapq.heappush(max_heap, -diff)
                bricks -= diff
                
                # If we run out of bricks, we need to use ladders
                if bricks < 0:
                    if ladders > 0:
                        # Use a ladder for the largest brick usage so far (invert back to get original value)
                        bricks += -heapq.heappop(max_heap)
                        ladders -= 1
                    else:
                        return i  # We can't go further
            
        return len(heights) - 1  # We can reach the last building
        