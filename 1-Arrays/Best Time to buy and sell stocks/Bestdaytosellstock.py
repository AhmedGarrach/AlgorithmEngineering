class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price=prices[0]
        max_profit=0
        for x in prices:
            if(min_price>x):
                min_price=x
            else:
                if(max_profit<x-min_price):
                    max_profit=x-min_price
        return max_profit