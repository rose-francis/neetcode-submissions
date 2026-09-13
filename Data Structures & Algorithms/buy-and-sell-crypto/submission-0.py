class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        l=len(prices)
        for i in range(l-1):
            for j in range(i+1,l):
                profit=prices[j]-prices[i]
                if profit>maxp:
                    maxp=profit
        return maxp
        