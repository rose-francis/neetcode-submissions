class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count=[0]*26
        d=[0]*26
        if len(s)!=len(t):
            return False
        for i in s:
            count[ord(i)-ord('a')]+=1
        for j in t:
            count[ord(j)-ord('a')]-=1
        return count==d
        