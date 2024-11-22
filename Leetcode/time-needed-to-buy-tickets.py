class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tot = 0
        for i,val in enumerate(tickets):
            if i < k:
                tot += min(tickets[k], val)
            elif i > k:
                tot += min(val, tickets[k]-1)
            else:
                tot += tickets[k]

