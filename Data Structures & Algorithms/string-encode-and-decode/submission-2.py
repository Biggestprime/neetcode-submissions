class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = str(len(strs))

        sizes_str = ""
        words = ""
        for sr in strs:
            sizes_str += str(len(sr)) + "-"
            words+=sr

        return encoded_str + "-" + sizes_str + words


    def decode(self, s: str) -> List[str]:
        number_of_words = int (s[0: s.index('-')])

        words_size = []
        index = s.index('-') + 1  
        for word_num in range(number_of_words):
            word_size = 0
            while(s[index] != '-'):
                word_size = word_size * 10 + int(s[index])
                index+=1

            words_size.append(word_size)
            index+=1    
               
        strs = []
        for size in words_size:
            strs.append(s[index : index + size])
            index = index + size

        return strs

