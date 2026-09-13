class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        resLen=0
        map={}
        for r in range(len(s)):
            map[s[r]]=map.get(s[r],0)+1
            
            maxv=max(map.values())
                    
            
            if (r-l+1-maxv)<=k and r-l+1>resLen:
                resLen=r-l+1
            
            while (r-l+1-maxv)>k:
                map[s[l]]-=1
                l+=1

                maxv=max(map.values())
                
        
        return resLen

                