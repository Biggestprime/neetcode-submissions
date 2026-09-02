class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        for ch in s1:
            freq[ch] = freq.get(ch, 0) + 1

        n = len(s2)
        l, r = 0, 0

        while r < n:
            while l < r and (s2[r] not in freq or freq[s2[r]] == 0):
                freq[s2[l]] = freq[s2[l]] + 1
                l+=1
    
            if s2[r] not in freq:
                r+=1
                l=r
            elif freq[s2[r]] > 0:
                freq[s2[r]] = freq[s2[r]] - 1
                r+=1

            if max(freq.values()) == 0:
                return True        

        return False 


# if s2[r] not in s1: r+=1, l = r         
