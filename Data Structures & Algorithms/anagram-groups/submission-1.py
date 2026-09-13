class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicti={}
        anagram=[]
        for i,a in enumerate(strs):
            e="".join(sorted(a))
            if e in dicti:
                dicti[e].append(strs[i])
            else:
                dicti[e]=[strs[i]]
        for j in dicti:
            anagram.append(dicti[j])
        return anagram
            
            




        