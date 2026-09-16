import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()
        l, r = 0, 0

        while r < len(nums):
            # keep only bigger numbers than me and comes before me in the original array
            # decresing order queue
            while q and nums[r] > nums[q[-1]]:
                q.pop()

            q.append(r)

            if q[0] < l:
                q.popleft() 

            if r + 1 >= k:
                result.append(nums[q[0]])
                l+=1    
        
            r+=1
        return result        





