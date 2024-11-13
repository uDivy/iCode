class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = {}
        
        # Create frequency dictionary
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1
        
        # Iterate through the string to find the index of the first unique character
        for index, char in enumerate(s):
            if frequency[char] == 1:
                return index  # Return the index of the first unique character
        
        return -1  # Return -1 if no unique character exists