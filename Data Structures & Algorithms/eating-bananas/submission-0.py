class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_ans = int(1e9) + 1

        while l <= r:
            mid = l + (r - l) // 2
            
            cnt = 0
            for pile in piles:
                cnt += math.ceil(pile / mid)


            if cnt <= h:
                r = mid - 1
                min_ans = mid
            else:
                l = mid + 1

        return min_ans        

        


       