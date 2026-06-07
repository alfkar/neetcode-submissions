class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        l_min = prices[l]
        while l<=r:
            l_min = min(l_min, prices[l])
            if l == r:
                r+=1
            else:
                l+=1
            if r < len(prices):
                max_profit=(max(max_profit, prices[r]-l_min))
            if l >= len(prices) -1:
                break
        return max_profit