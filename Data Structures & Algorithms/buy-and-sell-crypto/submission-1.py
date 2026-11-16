class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mn = 101
        for i in range(len(prices)):
            if prices[i] >= mn:
               continue
            mn = prices[i]   
            j = i + 1
            while j < len(prices):
                ans = max(ans, prices[j] - prices[i])
                j+=1
        
        return ans