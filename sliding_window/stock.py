# Problem 1 — Best Time to Buy and Sell Stock (LC 121, Easy)
# You're given an integer array prices, where prices[i] is the price of a stock on day i.
# Pick one day to buy and a later day to sell, so that profit is maximized. Return that maximum profit. If no profitable transaction exists, return 0.
# Example 1:
# Input:  prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price 1), sell on day 5 (price 6). Profit = 6 - 1 = 5.
# Note: buying at 1 and "selling" at 7 is invalid — day 1 comes before day 2.

# Example 2:
# Input:  prices = [7,6,4,3,1]
# Output: 0
# Explanation: Prices only fall; no transaction, profit 0.
# Constraints: 1 <= prices.length <= 10^5, 0 <= prices[i] <= 10^4

class Solution:
    def best_stock(self,arr)->int:
        l,r = 0,1
        max_profit = 0
        while (r<len(arr)):
            if(arr[r]<arr[l]):
                l = r
            else:
                max_profit = max(arr[r]-arr[l],max_profit)
            r+=1
        return max_profit            
        
s1 = Solution()
print(s1.best_stock([7,6,4,3,1]))