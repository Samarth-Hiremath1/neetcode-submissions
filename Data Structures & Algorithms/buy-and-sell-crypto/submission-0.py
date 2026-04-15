class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mProfit = 0
        
        lowest = prices[0]
        
        for price in prices:
            if price < lowest:
                lowest = price
            mProfit = max(mProfit, price - lowest)
        return mProfit