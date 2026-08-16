class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

    
        for i in range(len(s)):
            if t[i] not in countT:
                countT[t[i]] = 1
            else:
                countT[t[i]] += 1
            if s[i] not in countS:
                countS[s[i]] = 1
            else:
                countS[s[i]] += 1
        
        print(countS)
        print(countT)

        
        return countS == countT
