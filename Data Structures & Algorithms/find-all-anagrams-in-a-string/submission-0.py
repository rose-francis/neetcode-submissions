class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res=[]
        countP,countS=[0]*26,[0]*26
        for c in p:
            countP[ord(c)-ord('a')]+=1
        
        l=0
        for r in range(len(s)):
            countS[ord(s[r])- ord('a')]+=1

            if (r-l+1)>len(p):
                countS[ord(s[l])-ord('a')]-=1
                l+=1

            if countS==countP:
                res.append(l)
            
        return res