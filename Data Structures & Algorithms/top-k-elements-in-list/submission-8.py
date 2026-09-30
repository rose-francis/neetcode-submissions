class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        freq=defaultdict(int)
        buckets=[[] for i in range(n+1)]
        for num in nums:
            freq[num]+=1
        for key,v in freq.items():
            buckets[v].append(key)
        
        res=[]
        for i in range(len(buckets)-1,0,-1):
            for a in buckets[i]:
                res.append(a)
                if len(res)==k:
                    return res
        
    
        
