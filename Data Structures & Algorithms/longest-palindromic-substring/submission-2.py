class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=-1
        length=0
        for i in range(len(s)):
            l=i
            r=i
            while l-1>=0 and r+1<len(s):
                if s[l-1]==s[r+1]:
                    l-=1
                    r+=1
                else:
                    break
            
            if r-l+1>length:
                length=r-l+1
                res=l

            if i+1<len(s) and s[i]==s[i+1]:
                l=i
                r=i+1
                while l-1>=0 and r+1<len(s):
                    if s[l-1]==s[r+1]:
                        l-=1
                        r+=1
                    else:
                        break


            if r-l+1>length:
                length=r-l+1
                res=l
        return s[res:res+length]

        
