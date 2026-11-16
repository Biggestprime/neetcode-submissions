class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        mp = {}
        l, r = 0, 0
        while r < len(s):
            mp[s[r]] = mp.get(s[r], 0) + 1
            while l < r and mp[s[r]] > 1:
                mp[s[l]] -= 1
                l+=1
            ans = max(ans, r - l + 1)
            r+= 1
        return ans