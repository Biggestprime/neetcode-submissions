class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for st in strs:
            result = result + str(len(st)) + "_" + st
        return result  


    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        while i < len(s):
            j = s.find("_", i)
            if not s[i: j]:
                break
            length = int(s[i: j])
            
            words.append(s[j+1:j+1+length])
            i = j+1+length
        
        return words   

