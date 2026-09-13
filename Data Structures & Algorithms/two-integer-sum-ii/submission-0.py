class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while left<right:
            sum=numbers[left]+numbers[right]
            if sum==target:
                index1=left+1
                index2=right+1
                break
            elif sum<target:
                left+=1
            else:
                right-=1
        return [index1,index2]

        