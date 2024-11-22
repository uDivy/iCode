from typing import List
from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)  # Use deque for efficient pop from front
        stack = sandwiches
        last_served = 0
        
        while queue and last_served < len(stack):
            if queue[0] == stack[0]:  # If the first student matches the top sandwich
                queue.popleft()  # Serve the sandwich
                stack.pop(0)  # Remove the sandwich from the stack
                last_served = 0  # Reset last served counter
            else:
                queue.append(queue.popleft())  # Move the student to the back
                last_served += 1  # Increment last served counter
        
        return len(queue)  # Return the number of students unable to eat
        