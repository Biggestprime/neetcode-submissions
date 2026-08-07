class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        max = 0
        fleets = 0
        for p, s in pairs:
            reach_time = (target - p) / s
            if reach_time > max:
                fleets+=1
                max = reach_time
        return fleets


## 0 1 4 7
## 1 2 2 1
# target = 10
# 
# max = 5
# count = 3

# 1 2 3 4 5 6 7 8 9 10
