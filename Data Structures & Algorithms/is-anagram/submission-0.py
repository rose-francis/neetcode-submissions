class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        dicti={}
        for x in s:
            dicti[x]=dicti.get(x,0)+1
        
        for c in t:
            if c in dicti:
                dicti[c]-=1
                if dicti[c]==0:
                    del dicti[c]
            else:
                return False
            
        return dicti=={}
            
        


        