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
                #highest_freq = max(freq.values()) we remove this becuase of the fact that we only get a better
                # result only if we are removing from non highest freq, but if we remove at least of from most frequent letter, 
                # we aren't going to get a better result and therefore no issue with stale value of highest_freq
            mx = max(mx, r - l + 1)
            r+=1 
        return mx    

        



