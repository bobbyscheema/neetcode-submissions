import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

       
       count = Counter(nums)
       top = heapq.nlargest(k, count, key=count.get)

       return top
    




        

        

     