class Solution:

    def encode(self, strs: List[str]) -> str:
        enc=""
        for i in strs:
            enc+=str(len(i))+"#"+i
        return enc
        
    def decode(self, s: str) -> List[str]:
        cut=0
        deco=[]
        i=0
        while i<len(s):
            if s[i]=="#":
                l=int(s[cut:i])
                word=s[i+1:i+l+1]
                deco.append(word)
                i+=l+2
                cut=i-1
            else:
                i+=1
        return deco
            


                
