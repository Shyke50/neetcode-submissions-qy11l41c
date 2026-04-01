class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapp = {}
        
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in mapp and mapp[s[r]] >= l:
                l = mapp[s[r]] + 1
            mapp[s[r]] = r

            res = max(res, r - l + 1)
        return res