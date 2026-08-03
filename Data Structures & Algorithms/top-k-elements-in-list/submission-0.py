class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for number in nums:
            f = freq.get(number, 0)
            freq[number] = f + 1


        sorted_freq = dict(sorted(freq.items(), key=lambda x:x[1], reverse= True))
        return list(sorted_freq.keys())[:k]   

