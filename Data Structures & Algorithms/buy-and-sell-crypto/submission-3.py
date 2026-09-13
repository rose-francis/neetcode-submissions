class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        maxP=0
        for sell in prices:
            maxP=max(maxP, sell-buy)
            buy=min(sell,buy)
        return maxP