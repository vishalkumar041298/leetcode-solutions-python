class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0

        buy = prices[0]

        for sell in prices[1:]:
            if buy > sell:
                buy = sell
            maxp = max(sell - buy, maxp)
        
        return maxp
