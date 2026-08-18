class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p,s in zip(position, speed)]
        pairs.sort()
        stack = []
        for p, s in pairs:
            reach_time = (target - p) / s
            
            while len(stack) >= 1 and reach_time >= stack[-1]:
               stack.pop()
            stack.append(reach_time)   

        return len(stack)


## 0 1 4 7
## 1 2 2 1
# target = 10
# 3 4.5 5 
#

# 1 2 3 4 5 6 7 8 9 10
