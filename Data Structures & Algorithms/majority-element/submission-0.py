class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {} 

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        for c in counts:
            if counts.get(c) > (len(nums) / 2):
                return c

