class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1
        
        while left < right:
            sm = numbers[left] + numbers[right]
            if  sm == target:
                return [left+1, right+1]
            elif sm < target:
                left+=1
            else:
                right-=1
            
        return [-1, -1]  