class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        indices_to_remove = set()

        # Traverse the string to find invalid parentheses
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    indices_to_remove.add(i)

        # Add remaining '(' indices to remove
        indices_to_remove.update(stack)

        # Build the result string
        result = ''.join(char for i, char in enumerate(s) if i not in indices_to_remove)
        return result