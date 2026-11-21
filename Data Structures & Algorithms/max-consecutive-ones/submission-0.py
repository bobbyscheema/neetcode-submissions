class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_curr, res = 0, 0

        for n in nums:
            if n == 1:
                max_curr += 1
            else:
                max_curr = 0
            res = max(max_curr, res)

        return res