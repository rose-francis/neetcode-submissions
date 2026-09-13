class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP=0
        for i in range(len(prices)):
            m=max(prices[i+1:]) if i+1 <len(prices) else 0
            if m>prices[i] and m-prices[i]>maxP:
                maxP=m-prices[i]
        return maxP