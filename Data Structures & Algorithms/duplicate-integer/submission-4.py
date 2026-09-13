class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elements={}
        for i in nums:
            count=0
            for j in nums:
                if i==j:
                    count+=1
            elements[i]=count
        
        for k in elements:
            if elements[k]>1:
                return True
        return False
        
                
            