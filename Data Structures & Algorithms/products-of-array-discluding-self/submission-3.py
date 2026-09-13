class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro=1
        out=[0]*len(nums)
        zero=0

        for a in nums:
            if a==0:
                zero+=1
            else:
                pro*=a
        
        if zero>1:
            return out
        
        for i,a in enumerate(nums):
            if zero:
                if not a:
                    out[i]=pro
            else:
                out[i]=int(pro/a)
                    


        return out
        
        

        