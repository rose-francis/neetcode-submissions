class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list);
        for e in strs:
            count=[0]*26
            for i in e:
                count[ord(i)-ord('a')]+=1
            d[tuple(count)].append(e)
        
        return list(d.values())