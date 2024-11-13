# incomplete
from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Step 1: Sort the meetings based on the time
        meetings.sort(key=lambda x: x[2])  # Assuming meetings are in the format [person1, person2, time]

        # Step 2: Initialize the Union-Find structure
        parent = list(range(n))
        rank = [1] * n

        # Function to find the root of a person
        def find(person):
            if parent[person] != person:
                parent[person] = find(parent[person])  # Path compression
            return parent[person]

        # Function to union two people
        def union(person1, person2):
            root1 = find(person1)
            root2 = find(person2)
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1

        # Edge case: Handle the first person who knows the secret
        people_with_secret = {0, firstPerson}  # Include person 0 who always knows the secret

        # Iterate over the meetings and union the people who meet
        for meeting in meetings:
            person1, person2, time = meeting  # Unpacking with time included
            if time <= meetings[0][2]:  # Only union if the meeting time is before or equal to the first meeting time
                union(person1, person2)

        # Find all people who have the secret
        for person in range(n):
            if find(person) == find(0):  # Check if they are connected to person 0
                people_with_secret.add(person)

        # New logic to propagate the secret after processing all meetings
        for meeting in meetings:
            person1, person2, time = meeting
            if (person1 in people_with_secret or person2 in people_with_secret):
                people_with_secret.add(person1)
                people_with_secret.add(person2)

        return list(people_with_secret)  # Return the final list of people with the secret

# Test the function with the provided example
n = 6
meetings = [[1, 2, 5], [2, 3, 8], [1, 5, 10]]
firstPerson = 1

solution = Solution()
result = solution.findAllPeople(n, meetings, firstPerson)
print(result)  # Output the result

        