from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])  # Sort meetings by starting time
        min_heap = list(range(n))  # Initialize min heap representing room numbers from 0 to n-1
        heapq.heapify(min_heap)

        mostUsed = 0  # Initialize variable mostUsed
        room_count = [0] * n  # Track the number of meetings assigned to each room
        ongoing_meetings = []  # Min heap for ongoing meetings based on end time

        for start, end in meetings:  # Loop through each meeting
            # Free up rooms that have finished their meetings
            while ongoing_meetings and ongoing_meetings[0][0] <= start:
                _, room = heapq.heappop(ongoing_meetings)  # Free up the room

                # Push the room back to the min_heap
                heapq.heappush(min_heap, room)

            if min_heap:  # If there are available rooms
                room = heapq.heappop(min_heap)  # Assign to the first available room
                room_count[room] += 1  # Increment the count for the assigned room
                heapq.heappush(ongoing_meetings, (end, room))  # Add to ongoing meetings
            else:  # If no rooms are available
                # Get the room with the smallest end time
                end_time, room = heapq.heappop(ongoing_meetings)
                room_count[room] += 1  # Increment the count for the assigned room
                new_meeting_end = end_time + (end - start)  # Modify meeting to start from current end time
                heapq.heappush(ongoing_meetings, (new_meeting_end, room))  # Push the new meeting to ongoing meetings

            # Check for the room for which maximum meeting is assigned so far
            # If you find more than 1 such rooms take the room with lowest number
            if room_count[room] > room_count[mostUsed]:
                mostUsed = room
            elif room_count[room] == room_count[mostUsed]:
                mostUsed = min(mostUsed, room)
        
        return mostUsed
    
# Test the code with the provided list of meetings
solution = Solution()
meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
n = 3  # Number of rooms
result = solution.mostBooked(n, meetings)
print(result)  # Output the result     