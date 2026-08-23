class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""

        for s in strs:
            new_str += str(len(s)) + "#" + s
        return new_str

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1 
            length = int(s[i:j]) # gets the len(s) encoded
            result.append(s[j + 1: j + 1 + length]) # add next word
            i = j + 1 + length # go to next word
        return result          