from typing import List
from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency_map = Counter(tasks)
        max_heap = [(-count, task) for task, count in frequency_map.items()]
        heapq.heapify(max_heap)
        
        intervals = 0
        
        while max_heap:
            cooldown_period = n + 1
            queue = []
            while cooldown_period > 0 and max_heap:
                count, task = heapq.heappop(max_heap)
                count += 1
                intervals += 1
                if count != 0:
                    queue.append((count, task))
                cooldown_period -= 1
                
            if queue:
                intervals += cooldown_period
                for item in queue:
                    heapq.heappush(max_heap, item)
                    
        return intervals