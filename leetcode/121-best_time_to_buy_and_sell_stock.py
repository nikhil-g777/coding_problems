class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        
        max_profit = 0
        current_min = prices[0]
        
        for price in prices:
            current_min = min(current_min, price) # keep updating current min
            max_profit = max(max_profit, price - current_min) # update max profit as difference between price and the minimum seen so far
        
        return max_profit