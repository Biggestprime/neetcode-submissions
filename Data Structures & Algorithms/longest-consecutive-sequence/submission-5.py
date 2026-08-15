class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq_nums = set()
        for num in nums:
           uniq_nums.add(num)
        
        mx = 0  
        for num in nums:
            if num - 1 not in uniq_nums:
                temp = num
                while temp in uniq_nums:
                    temp+=1             
                mx = max(mx, temp - num)      
        
        return mx  

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

