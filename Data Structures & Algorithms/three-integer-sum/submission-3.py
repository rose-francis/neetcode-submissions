class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets=[]
        left=0
        right=len(nums)-1
        nums.sort()

        for i in range(len(nums)-2):
            t=-nums[i]

            if i>0 and nums[i]==nums[i-1]:
                continue

            left=i+1
            right=len(nums)-1
            while left<right:
                sum=nums[left]+nums[right]
                if sum<t:
                    left+=1
                elif sum>t:
                    right-=1
                else:
                    triplets.append([nums[left],nums[right],nums[i]])

                    while left <right and nums[left]==nums[left+1]:
                        left+=1
                    
                    while left< right and nums[right]==nums[right-1]:
                        right-=1
                        
                    left+=1
                    right-=1
        return triplets


        