class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        
        queue = list(range(len(deck)))
        answer = [0] * len(deck)
        ptr = 0
        
        while queue:
            index = queue.pop(0)
            answer[index] = deck[ptr]
            ptr += 1
            if queue:
                queue.append(queue.pop(0))
                
        return answer