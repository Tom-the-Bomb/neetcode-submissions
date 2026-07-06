class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        max_p = 0

        for price in prices:
            max_p = max(max_p, price - min_p)
            min_p = min(min_p, price)
        return max_p