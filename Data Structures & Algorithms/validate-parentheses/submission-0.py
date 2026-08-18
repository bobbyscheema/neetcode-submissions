class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        
        for i in range(len(s)):
            stack.append(s[i])
            for c in s:
                if ["())", "[]", "{}"] in stack:
                    stack.pop()
                       
                
        return len(stack) != 0 # if "}" left (incomplete) return false

                
                    