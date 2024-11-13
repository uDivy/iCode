from collections import Counter
import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Count the frequency of each element
        frequency = Counter(arr)
        
        # Create a min heap based on the frequency
        min_heap = list(frequency.values())
        heapq.heapify(min_heap)

        # Start removing elements from the heap
        while k > 0 and min_heap:
            # Remove the smallest frequency element
            smallest_freq = heapq.heappop(min_heap)
            k -= smallest_freq  # Reduce k by the frequency of the removed element
            
            # If k is negative, we need to push back the last element
            if k < 0:
                heapq.heappush(min_heap, smallest_freq)

        # Return the number of unique elements remaining in the heap
        return len(min_heap)
        