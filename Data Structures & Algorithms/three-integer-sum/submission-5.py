class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if nums[j+1]<nums[j]:
                    temp=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp

        res=[]
        for i in range(len(nums)):

            if i>0 and nums[i]==nums[i-1]:
                continue

            l=i+1
            r=len(nums)-1

            while l<r:
                if nums[l]+nums[r]<-nums[i]:
                    l+=1
                elif nums[l]+nums[r]>-nums[i]:
                    r-=1
                else:
                    res.append([nums[l],nums[r],nums[i]])
                    r-=1
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        
        return res


