class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        f1=[0] * 26
        f2= [0] * 26

        for i in s1:
            f1[ord(i)- ord('a')]+=1
        
        l=0
        r=l+len(s1)-1

        while r<len(s2):
            for j in range(l,r+1):
                idx=ord(s2[j]) - ord('a')
                if f1[idx]!=0:
                    f2[idx]+=1
            if f1==f2:
                return True
            
            l+=1
            r+=1
            f2=[0]*26

        return False
            

        
        