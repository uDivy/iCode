from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Create an array to count trust relationships
        trust_count = [0] * (n + 1)  # Index 0 is unused
        
        # Loop through the trust list
        for a, b in trust:
            trust_count[a] -= 1  # a trusts someone, so decrease their count
            trust_count[b] += 1   # b is trusted by someone, so increase their count
        
        # Find the judge
        for person in range(1, n + 1):
            if trust_count[person] == n - 1:  # Judge should be trusted by n-1 people
                return person
        
        return -1  # No judge found
                