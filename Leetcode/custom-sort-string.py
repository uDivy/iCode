class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_index = {char: index for index, char in enumerate(order)}
        reorder_s = {}
        for char in s:
            index = order_index.get(char, len(s))
            reorder_s[index] = reorder_s.get(index, '') + char
        
        return ''.join(reorder_s[i] for i in sorted(reorder_s))
        