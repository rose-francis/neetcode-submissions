class Solution:
    def hasDuplicate(self, num: List[int]) :
        hashset=set()
        for i in num:
            if i in hashset:
                return True
            hashset.add(i)
        return False