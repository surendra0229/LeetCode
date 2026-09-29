class Solution(object):
    def maxProfit(self, prices):
        MinimumPrice = prices[0]
        MaximumProfit = 0

        for price in prices :
            MinimumPrice = min(price, MinimumPrice)
            MaximumProfit = max(MaximumProfit, price-MinimumPrice)

        return MaximumProfit