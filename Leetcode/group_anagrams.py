from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a defaultdict to hold lists of anagrams
        """
        Groups anagrams from a list of strings.

        Time Complexity: O(N * K), where N is the number of strings and K is the maximum length of a string.
        Space Complexity: O(N * K) for storing the anagrams in the dictionary.
        """
        
        anagrams = defaultdict(list)

        # Iterate over each string in strs
        for s in strs:
            # Create a frequency dictionary for characters in the string
            temp_alphabet_dict = {char: 0 for char in 'abcdefghijklmnopqrstuvwxyz'}
            for char in s:
                temp_alphabet_dict[char] += 1  # Increment the count for each character
            
            # Create a key based on the frequency of characters
            key = '*'.join(str(temp_alphabet_dict[char]) for char in 'abcdefghijklmnopqrstuvwxyz')
            print(key)
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]

        return list(anagrams.values())