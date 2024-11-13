import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Sorts characters in the string `s` by their frequency in descending order.

        Time Complexity:
        - O(n log n): where n is the length of the string `s`. This is due to the heap operations
          when creating the max heap and popping elements from it.

        Space Complexity:
        - O(n): for storing the frequency dictionary and the max heap, which can contain up to n characters.
        """
        # Initialize an empty dictionary to store character frequencies
        freq_char = {}
        
        # Fill freq_char with character frequencies
        for char in s:
            freq_char[char] = freq_char.get(char, 0) + 1
        
        # Create a max heap of tuples (frequency, character)
        max_heap = [(-freq, char) for char, freq in freq_char.items()]
        heapq.heapify(max_heap)
        
        # Create a string by popping each element from the heap
        result = ''
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result += char * (-freq)  # Append the character -freq times
        
        return result
        
        