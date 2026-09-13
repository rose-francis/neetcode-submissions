class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        max_len=0
        mp={}
        for r in range(len(s)):
            if s[r] in mp:
                l=max(mp[s[r]]+1, l)
            mp[s[r]]=r
            max_len=max(max_len,r-l+1)
        return max_len
                
                
