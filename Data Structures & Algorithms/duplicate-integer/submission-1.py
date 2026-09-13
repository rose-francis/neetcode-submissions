class Solution:
    def hasDuplicate(self, num: List[int]) :
        hashset = set()

        for n in num:
            if n in hashset:
                return True
            hashset.add(n)
        return False