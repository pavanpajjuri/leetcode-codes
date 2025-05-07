class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_min = prices[0]
        for price in prices:
            if price >= curr_min:
                max_profit = max(max_profit, price - curr_min)
            else:
                curr_min = min(curr_min, price)
        return max_profit