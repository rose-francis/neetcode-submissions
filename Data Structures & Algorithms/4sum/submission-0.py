class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-3):
            n=target-nums[i]
            for j in range(i+1,len(nums)-2):
                n2=n-nums[j]
                l=j+1
                r=len(nums)-1
                while l<r:
                    if nums[l]+nums[r]==n2:
                        res.append((nums[i],nums[j],nums[l],nums[r])) 
                        l+=1
                        r-=1
                    elif nums[l]+nums[r]<n2:
                        l+=1
                    else:
                        r-=1
        
        return list(set(res))
