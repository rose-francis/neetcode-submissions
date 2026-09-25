class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        if amount in coins:
            return 1
        if amount%max(coins)==0:
            return amount//max(coins)
        
        minCount=float("infinity")
        q=deque([amount])
        count=0
        visited=set()
        visited.add(amount)
        while q:
            l=len(q)
            count+=1
            for _ in range(l):
                cur=q.popleft()
                for n in coins:
                    if cur-n==0:
                        minCount=min(count,minCount)
                    elif cur-n>0:
                        if (cur-n) not in visited:
                            q.append(cur-n)
                            visited.add(cur-n)
        if minCount!=float("infinity"):
            return minCount
        else:
            return -1
                    

