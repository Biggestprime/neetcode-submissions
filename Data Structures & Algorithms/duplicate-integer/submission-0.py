class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for index, number in enumerate(nums):
            if index > 0 and nums[index - 1] == number:
                return True
        
        return False