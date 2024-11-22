class Solution:
    def checkValidString(self, s: str) -> bool:
        open_count = 0
        close_count = 0
        length = len(s)
        
        for i in range(length):
            if s[i] == '(' or s[i] == '*':
                open_count += 1
            else:
                open_count -= 1
            
            if s[length - 1 - i] == ')' or s[length - 1 - i] == '*':
                close_count += 1
            else:
                close_count -= 1
            
            if open_count < 0 or close_count < 0:
                return False
        
        return True