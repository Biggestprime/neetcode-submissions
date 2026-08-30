class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        n = len(s)
        l, r = 0, 0
        mx = 0

        while r < n:
            freq[s[r]] = freq.get(s[r], 0) + 1
            
            highest_freq = max(freq.values())
            while r - l + 1 - highest_freq > k:
                freq[s[l]] = freq[s[l]] - 1
                l+=1
                highest_freq = max(freq.values())
            mx = max(mx, r - l + 1)
            r+=1 
        return mx    

        



