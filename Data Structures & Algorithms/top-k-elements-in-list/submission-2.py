class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                freq = count.get(num, 1)
                count[num] = freq + 1
            
        result = []
        freq = [[] for _ in range(len(nums) + 1)]

        for key, value in count.items():
            freq[value].append(key)
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result
            
        
        

    