class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res=[]
       
        for i,a in enumerate(nums):
            if a>0:
                break

            if i>0 and nums[i-1]==a:
                continue

            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[l]+nums[r]==-nums[i]:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l-1]==nums[l] and l<r:
                        l+=1
                elif nums[l]+nums[r]<-nums[i]:
                    l+=1
                else:
                    r-=1

            
        return res