from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicti=defaultdict(int)
        tdict=defaultdict(int)
        if len(s)!=len(t):
            return False
        for i in s:
            dicti[i]+=1
        for j in t:
            tdict[j]+=1
        return dicti==tdict
        