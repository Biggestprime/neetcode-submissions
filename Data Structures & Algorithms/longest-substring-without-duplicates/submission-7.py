class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        mp = {}
        l = 0

        for r in range(len(s)):
            if s[r] in mp:
               l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            ans = max(ans, r - l + 1)
        return ans         