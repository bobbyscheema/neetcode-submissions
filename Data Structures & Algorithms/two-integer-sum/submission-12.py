class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        not_set = {}

        for i, value in enumerate(nums):
            if target - value in not_set:
                return [not_set[target - value], i]
            not_set[value] = i


