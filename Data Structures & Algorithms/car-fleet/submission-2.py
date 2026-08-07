class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []

        for p, s in pairs:
            reach_time = (target - p) / s
            stack.append(reach_time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


## 0 1 4 7
## 1 2 2 1
# target = 10
# 3 4.5 5 
#

# 1 2 3 4 5 6 7 8 9 10
