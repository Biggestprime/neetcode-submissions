class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return  0
        if len(s) == 1:
            return 1    
        mx = 0
        l, r = 0, 1
        n = len(s)
        freq = {} 
        freq[s[l]] = 1

        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1 
            while freq[s[r]] > 1:
                freq[s[l]]-=1
                l+=1

            mx = max(mx, r - l + 1)  
            r+=1
               
        return mx