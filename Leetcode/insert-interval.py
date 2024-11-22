class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        for interval in intervals:
            # Check for overlap
            if interval[1] < newInterval[0]:  # No overlap, interval ends before newInterval starts
                merged.append(interval)
            elif interval[0] > newInterval[1]:  # No overlap, interval starts after newInterval ends
                merged.append(newInterval)
                newInterval = interval  # Update newInterval to the current interval
            else:  # Overlap exists
                newInterval[0] = min(newInterval[0], interval[0])  # Update start
                newInterval[1] = max(newInterval[1], interval[1])  # Update end
        merged.append(newInterval)  # Add the last merged interval
        return merged
        