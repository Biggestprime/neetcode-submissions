class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                if left > i +1 and nums[left] == nums[left-1]:
                   left+=1
                   continue
                if right < n - 1 and nums[right] == nums[right+1]:
                    right-=1
                    continue     
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                elif sum > 0:
                    right-=1
                else:
                    left+=1
        return result