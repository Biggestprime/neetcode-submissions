class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        ans = 1001

        while l <= r:
            mid = l + (r - l) // 2

            if nums[l] < nums[r]:
                if nums[mid] > nums[l]:
                    return nums[l]
                else:
                    ans = min(ans, nums[mid])
                    r = mid - 1
            else:
                if nums[mid] <= nums[r]:
                    ans = min(ans, nums[mid])
                    r = mid - 1
                else:
                    l = mid + 1

        return ans            


