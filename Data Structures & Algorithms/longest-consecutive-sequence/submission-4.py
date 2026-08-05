class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        max_subsequence = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                current = num
                count = 0
                while(current in nums_set):
                    count+=1
                    current+=1
                max_subsequence = max(max_subsequence, count)

        return max_subsequence    


## 2 20 4 10 3 4 5
## 2 3 4 4 5 10 20 
## 2 3 4 4 5
## 
##
## 
##
## brute force O(n^2)
## start lowest and eliminate O(nlog n) //sorting
## 

