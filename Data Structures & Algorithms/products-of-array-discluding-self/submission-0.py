class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # input, list of numbers - nums
        # ouput, product of nums except current nums[i]

        result = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result