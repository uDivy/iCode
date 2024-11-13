class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:  # Check if the word is equal to its reverse
                return word  # Return the first palindromic word
        return ""  # Return an empty string if no palindromic word is found
        