class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            match = {}
            for i, char in enumerate(s):
                match[char] = match.get(char, 0) + 1

            for j, char in enumerate(t):
                if char not in match or match[char] == 0:
                    return False                
                match[char] -= 1
            
            return True