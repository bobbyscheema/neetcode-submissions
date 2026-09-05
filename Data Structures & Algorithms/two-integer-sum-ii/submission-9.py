class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pairs = {}

        
        for i, value in enumerate(numbers, start=1):
            if target - value in pairs:
                return [pairs[target - value], i]
            pairs[value] = i 
        