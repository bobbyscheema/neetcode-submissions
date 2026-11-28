class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0

        for _ in range(len(prices) - 1):
            if prices[l] > prices[r]:
                l, r = r, r + 1
            elif prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
                r += 1
            else:
                r += 1
        return profit

        
            

            