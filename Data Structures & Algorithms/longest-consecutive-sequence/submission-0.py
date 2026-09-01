class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort = set(nums)
        result = 0

        for num in nums:
            streak = 0
            curr = num
            while curr in sort:
                streak += 1
                curr += 1
            result = max(result, streak)

        return result
