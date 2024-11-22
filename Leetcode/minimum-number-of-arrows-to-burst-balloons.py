class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:  # Check for empty input
            return 0
        
        points.sort(key=lambda x: x[0])  # Sort points by the start of the intervals
        arrows = 1  # Start with one arrow
        end = points[0][1]  # Initialize the end of the first interval
        
        for interval in points[1:]:  # Iterate through the intervals starting from the second
            if interval[0] > end:  # No overlap
                arrows += 1  # Need a new arrow
                end = interval[1]  # Update end to the current interval's end
            else:  # Overlap exists
                end = min(end, interval[1])  # Update end to the minimum end of overlapping intervals
        
        return arrows  # Return the number of arrows needed