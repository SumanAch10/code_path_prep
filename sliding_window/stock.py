
class Solution:
    def maxProfit(self,prices)->int:
        cheapest_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < cheapest_price:
                cheapest_price = price
            elif price - cheapest_price > max_profit:
                max_profit = price - cheapest_price
        
        return max_profit