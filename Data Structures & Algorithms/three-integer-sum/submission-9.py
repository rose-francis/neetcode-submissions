class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=[]
        n=len(nums)
        nums.sort()
        for i,a in enumerate(nums):
            if a>0:
                break
            
            if i>0 and a==nums[i-1]:
                continue

            j=i+1
            k=n-1
            while j<k:
                s=nums[j]+nums[k]
                if s==-nums[i]:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                elif s<-nums[i]:
                    j+=1
                else:
                    k-=1
        
        return res
            

