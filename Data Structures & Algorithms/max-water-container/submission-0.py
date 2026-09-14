class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # height of ith bar (y) = height[i]
        # goal - choose 2 bars to form container with max amount of water

        i = 0
        j = len(heights) - 1 
        max_water = 0
        while i < j:
            width, height = j - i, min(heights[i], heights[j])
            curr_max = width * height
        
            if max_water < curr_max:
                max_water = curr_max
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            
        
        return max_water
        



        