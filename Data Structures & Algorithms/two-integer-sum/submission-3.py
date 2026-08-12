class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_set = {}

        for i, value in enumerate(nums):
            if target - value in new_set:
                return [new_set[target - value], i]
            new_set[value] = i
        
        
        
    

