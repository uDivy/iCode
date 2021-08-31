def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        check = False
        length = len(s)
        if length == 1:
            return 1
        for k in s[1:]:
            if s[0] is k:
                count += 1
        if count == length-1:
            return 1
        count = 0
        for i in range(length-1):
            for j in range(i+1,length):
                substr = s[i:j+1]
                new_count = len(substr)
                for index, k in enumerate(substr, start=0):
                    temp = substr[0:index] + substr[index+1:new_count]
                    if k not in temp:
                        check = True
                    else:
                        check = False
                        break
                if check and new_count > count:
                    count = new_count
        return count



        ########### using sliding window ##########
        def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        length = len(s)
        if length == 1:
            return 1
        for k in s[1:]:
            if s[0] is k:
                count += 1
        if count == length-1:
            return 1
        substr = []
        i, j, ans = 0, 0, 0
        while i < length and j < length:
            if s[j] not in substr[i:]:
                substr.append(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                i += 1        
        return ans