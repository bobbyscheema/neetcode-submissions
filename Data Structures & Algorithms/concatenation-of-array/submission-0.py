class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []

        for i in nums * 2:
            result.append(i)
        
        return result

        