class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        count=defaultdict(int)
        l=maxN=0

        for r in range(len(fruits)):
            count[fruits[r]]+=1

            while len(count)>2:
                count[fruits[l]]-=1
                if count[fruits[l]]==0:
                    del count[fruits[l]]
                l+=1
            
            maxN=max(maxN, r-l+1)
        
        return maxN
