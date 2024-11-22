class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):  # Edge case: k is greater than or equal to the length of num
            return '0'  # Return '0' if all digits are to be removed
        if not num:  # Edge case: empty string
            return '0'  # Return '0' for empty input
        
        stack = []  # Initialize stack
        for digit in num:  # Go through the string
            while k > 0 and stack and stack[-1] > digit:  # Check conditions
                stack.pop()  # Pop the element from stack
                k -= 1  # Reduce k by 1
            stack.append(digit)  # Push the new number to stack
        if k:
            stack = stack[:-k]
        return ''.join(stack).lstrip('0') or '0'  # Create string from stack and return
        