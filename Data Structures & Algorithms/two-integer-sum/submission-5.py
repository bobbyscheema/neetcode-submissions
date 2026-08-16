class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        for key, value in enumerate(nums):
            if target - value in pairs:
                return [pairs[target - value], key]
            pairs[value] = key