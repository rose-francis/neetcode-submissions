class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for num in nums:
            new=[]
            for r in res:
                for i in range(len(r)+1):
                    r_copy=r.copy()
                    r_copy.insert(i,num)
                    new.append(r_copy)
            res=new
        return res

            
