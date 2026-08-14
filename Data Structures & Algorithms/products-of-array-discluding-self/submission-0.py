class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        curr = 1
        for i in range(len(nums)):
            prefix[i] = curr 
            curr *= nums[i]

        curr = 1
        for i in range(len(nums) - 1,-1,-1):
            suffix[i] = curr
            curr *= nums[i]

        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = prefix[i] * suffix[i]

        return output    


            