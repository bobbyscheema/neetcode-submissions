class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        for index, value in enumerate(nums):
            if target - value in pairs:
                return [pairs[target - value], index]
            pairs[value] = index

        return list(pairs.values())