class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappingStoT = {}
        mappingTtoS = {}

        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]

            if sChar not in mappingStoT:
                mappingStoT[sChar] = tChar

            if tChar not in mappingTtoS:
                mappingTtoS[tChar] = sChar

            if mappingStoT[sChar] != tChar or mappingTtoS[tChar] != sChar:
                return False

        return True