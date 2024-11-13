class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        start = 0  # Initialize start pointer
        end = len(s) - 1  # Initialize end pointer
        
        while start < end:  # Run the loop until start is less than end
            if s[start] == '1':
                start += 1  # Move start pointer if it sees a 1
            elif s[end] == '0':
                end -= 1  # Move end pointer if it sees a 0
            else:
                # Switch values at start and end pointers
                s_list = list(s)  # Convert string to list for mutability
                s_list[start], s_list[end] = s_list[end], s_list[start]  # Swap values
                s = ''.join(s_list)  # Convert list back to string
                start += 1  # Move start pointer
                end -= 1  # Move end pointer
        
        # Remove the value at the current start position and move it to the end
        if len(s) > 1:
            s = s[:start-1] + s[start:] + s[start-1]  # Exclude s[start] and append it to the end
        
        return s  # Return the modified string

# Example usage
solution = Solution()
output = solution.maximumOddBinaryNumber("0101")
print(output)  # Print the output
        