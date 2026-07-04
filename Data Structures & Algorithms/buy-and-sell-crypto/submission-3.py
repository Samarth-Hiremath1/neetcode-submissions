'''
buy low sell high



'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0
        
        l = 0
        for r in range(len(prices)):
            if (prices[l] < prices[r]):
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            
            if (prices[l] > prices[r]):
                l = r
            r += 1

        return maxP