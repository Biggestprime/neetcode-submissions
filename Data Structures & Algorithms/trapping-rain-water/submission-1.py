class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        n = len(height)
        for i in range(n):
            while stack and height[i] >= height[stack[-1]]:
                    bottom = height[stack.pop()]
                    if stack:
                        w = i - stack[-1] - 1
                        h = min(height[i], height[stack[-1]]) - bottom
                        res += w * h
            stack.append(i)
        return res