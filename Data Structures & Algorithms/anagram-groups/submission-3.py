class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for word in strs:
            l=[0]*26
            for i in word:
                l[ord(i)-ord('a')]+=1
            d[tuple(l)].append(word)
        return list(d.values())
