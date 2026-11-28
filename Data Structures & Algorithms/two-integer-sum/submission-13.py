class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, value in enumerate(nums):
            if target - value in hashmap:
                return [hashmap[target - value], i]
            hashmap[value] = i
        return []