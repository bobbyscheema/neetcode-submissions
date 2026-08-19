class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in openToClose: # if closed
                if stack and stack[-1] == openToClose[c]: # if not empty and matches remove from stack, valid parenthesis
                    stack.pop()  
                else:
                    return False # no matching, return false
            else:
                stack.append(c) # add as many open parenthesis 

        return True if not stack else False # if no leftover unmatched return True, otherwise return False
                
            