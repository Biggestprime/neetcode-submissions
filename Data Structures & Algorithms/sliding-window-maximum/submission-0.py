import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []
        result = []

        for i in range(len(nums)):
            heapq.heappush(pq, (-nums[i], i))
            if i >= k - 1:
                while pq[0][1] <= i - k:
                    heapq.heappop(pq)

                result.append(-pq[0][0]) 
        return result           

            



