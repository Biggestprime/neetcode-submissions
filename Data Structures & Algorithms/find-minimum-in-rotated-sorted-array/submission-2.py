class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        ans = 1001

        while l <= r:
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break

            mid = l + (r - l) // 2
            ans = min(ans, nums[mid])
            
            if nums[mid] <= nums[r]:
                r = mid - 1
            else:
                l = mid + 1
            
        return ans            


