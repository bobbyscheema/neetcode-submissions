class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        for i, value in nums:
            if target - value in pairs:
                return [pairs[target - value], i]
            pairs[value] = i
