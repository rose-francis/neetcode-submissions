class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        resLen=0
        map={}
        maxf=0
        for r in range(len(s)):
            map[s[r]]=map.get(s[r],0)+1
            
            maxf=max(maxf,map[s[r]])
            
            while (r-l+1-maxf)>k:
                map[s[l]]-=1
                l+=1

                maxf=max(maxf,map[s[l]])

            resLen=max(resLen,r-l+1)
        
        return resLen

                