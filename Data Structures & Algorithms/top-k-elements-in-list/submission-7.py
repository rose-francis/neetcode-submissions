class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=1+ count.get(num,0)
        
        freq_list=[[] for _ in range(len(nums)+1)]
        for i,c in count.items():
            freq_list[c].append(i)
        
        res=[]
        for i in range(len(freq_list)-1,0,-1):
            for num in freq_list[i]:
                res.append(num)
                if len(res)==k:
                    return res
