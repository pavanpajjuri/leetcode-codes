class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0]
        ans = 0
        n = len(prices)
        i = 1
        for i in range(1,n):   
            if prices[i] > min_:
                diff = prices[i] - min_
                ans = max(ans, diff)
            else:
                min_ = min(min_, prices[i])
        return ans