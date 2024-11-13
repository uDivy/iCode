class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Find the minimum window substring of `s` that contains all characters of `t`.

        Time Complexity: O(n + m), where n is the length of string `s` and m is the length of string `t`.
        This is because we traverse the string `s` with the right pointer and potentially the left pointer,
        leading to a linear scan of the string.

        Space Complexity: O(m), where m is the number of unique characters in `t`.
        This is due to the storage of character counts in the `char_count` and `window_count` dictionaries.
        """
        # Count characters in t
        char_count = {}
        for char in t:
            char_count[char] = char_count.get(char, 0) + 1
        window_count = {}
        left = 0
        right = 0
        min_length = float('inf')
        min_start = 0

        # Expand the window by moving the right pointer
        while right < len(s):
            # Add the current character to the window count
            window_count[s[right]] = window_count.get(s[right], 0) + 1
            
            # Check if the current window is valid
            while all(window_count.get(char, 0) >= char_count[char] for char in char_count):
                # Update the minimum window if needed
                current_length = right - left + 1
                if current_length < min_length:
                    min_length = current_length
                    min_start = left  # Track the start index of the minimum window
                
                # Contract the window by moving the left pointer
                window_count[s[left]] -= 1
                if window_count[s[left]] == 0:
                    del window_count[s[left]]
                left += 1
            
            right += 1

        return s[min_start:min_start + min_length] if min_length != float('inf') else ""
        