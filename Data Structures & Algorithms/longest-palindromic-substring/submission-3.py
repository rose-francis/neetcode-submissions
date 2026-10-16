class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=-1
        length=0
        for i in range(len(s)):
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) >length:
                    length=r-l+1
                    res=l
                l-=1
                r+=1

            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>length:
                    res=l
                    length=r-l+1
                l-=1
                r+=1
                   
        return s[res:res+length]

        
