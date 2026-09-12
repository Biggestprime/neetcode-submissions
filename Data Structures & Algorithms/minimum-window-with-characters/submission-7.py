class Solution:
    #convert freq arrays to map to handle lower and upper case characters
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""

        s_count, t_count = {}, {}
        l = 0
        for i in range(len(t)):
            t_count[t[i]] = t_count.get(t[i], 0) + 1
            s_count[s[i]] = s_count.get(s[i], 0) + 1

        matches = 0  
        for i in range(26):
            lower = chr(ord('a') + i)
            upper = chr(ord('A') + i)
            matches += 1 if s_count.get(lower, 0) >= t_count.get(lower, 0) or t_count.get(lower, 0) == 0 else 0
            matches += 1 if s_count.get(upper, 0) >= t_count.get(upper, 0) or t_count.get(upper, 0) == 0 else 0

        min_substring = ""

        for r in range(len(t), len(s)):
            #print(s[l:r] + ":" + str(matches))
            if matches == 52 and (r - l < len(min_substring) or len(min_substring) == 0):
                min_substring = s[l:r]

            s_count[s[r]] = s_count.get(s[r], 0) + 1
            if t_count.get(s[r], 0) == 0:
                continue

            if s_count.get(s[r], 0) == t_count.get(s[r], 0):
                matches += 1 

            while l < r and s_count.get(s[l], 0) > t_count.get(s[l], 0):
                s_count[s[l]] = s_count.get(s[l], 0) - 1
                # if s_count.get(s[l], 0) == t_count.get(s[l], 0):
                #     matches += 1
                # elif s_count.get(s[l], 0) + 1 == t_count.get(s[l], 0):
                #     matches -= 1      
                l += 1

        if matches == 52 and (len(s) - l < len(min_substring) or len(min_substring) == 0):
            min_substring = s[l:len(s)]

        return min_substring    

 # increase l only if doesn't decrease freq of c such that c exists in t and freq[c] in s < freq[c] in t
 # while freq[l] == 0 in t or freq[s[r]] in s > freq[s[r]] in c: increase l