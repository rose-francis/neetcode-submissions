class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicti={}
        for i in nums:
            if i in dicti:
                dicti[i]+=1
            else:
                dicti[i]=1
        print(dicti)
        max=[]
        for i in range(k):
            count=0
            for j in dicti:
                if dicti[j]>count:
                    count=dicti[j]
                    d=j
            del dicti[d]
            max.append(d)
        return max
            

            
