class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums)==0:
            return 0

        count=0
        num_set=set(nums)

        for i in num_set:
            if i-1 in num_set:
                continue
            
            l=0
            l+=1
            while True:
                if i+1 in num_set:
                    l+=1
                    i+=1
                else:
                    if l>count:
                        count=l
                    break
        
        return count

        