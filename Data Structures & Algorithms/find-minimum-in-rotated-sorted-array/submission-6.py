class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
    
        while l < r:
            mid = l + (r - l) // 2
            if nums[l] <= nums[mid] and nums[l] <= nums[r]:
               return nums[l]
            elif nums[mid] < nums[l] and nums[mid] < nums[r]:
               r = mid
            else: 
               l = mid + 1
        
        return nums[l]
        
        

 # if mid < left --> left
 # if right < mid --> right
 # if mid > left --> left
 # 12345
 # 23451
 # 45123
 # 51234
 # 34512
 # if left < mid and left < right
 #    ans = left 
 # if right < mid and right < left
 #     search right
 # 
 #  