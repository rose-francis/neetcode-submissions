class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for n in nums:
            count[n]=count.get(n,0)+1
        
        buckets=[[] for i in range(len(nums)+1)]
        for key,v in count.items():
            buckets[v].append(key)
        
        res=[]
        for b in range(len(buckets)-1,0,-1):
            for num in buckets[b]:
                res.append(num)
                if len(res)==k:
                    return res
