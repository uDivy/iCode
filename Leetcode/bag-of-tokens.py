from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()  # Step 1: Sort tokens
        first, last = 0, len(tokens) - 1  # Step 2: Initialize two pointers
        score, max_score_so_far = 0, 0  # Initialize score and max_score_so_far
        
        while first <= last:  # Step 3: Use two-pointer technique
            if power >= tokens[first]:  # Check if enough power to play face up
                power -= tokens[first]  # Reduce power
                score += 1  # Gain score
                max_score_so_far = max(max_score_so_far, score)  # Update max score
                first += 1  # Move left pointer
            elif score > 0:  # If not enough power but have score to gain power
                power += tokens[last]  # Gain power from the right
                score -= 1  # Reduce score
                last -= 1  # Move right pointer
            else:
                break  # Break if no moves are possible
        return max_score_so_far