class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        maxP=0
        for i in range(len(prices)):
            sell=prices[i+1] if i+1<len(prices) else 0
            if prices[i]<buy:
                buy=prices[i]
            if sell-buy>maxP:
                maxP=sell-buy
        return maxP