class Solution:

    def encode(self, strs: List[str]) -> str:
        enc=""
        for i in strs:
            enc+=str(len(i))+"#"+i
        return enc
        
    def decode(self, s: str) -> List[str]:
        deco=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            l=int(s[i:j])
            i=j+1
            j=i+l
            deco.append(s[i:j])
            i=j

        return deco
            


                
