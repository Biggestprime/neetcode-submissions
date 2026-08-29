class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:    
        mx = 0
        l, r = 0, 0
        n = len(s)
        elements = set()

        while r < len(s):
            while s[r] in elements:
                elements.remove(s[l])
                l+=1

            elements.add(s[r])    
            mx = max(mx, r - l + 1)  
            r+=1
               
        return mx