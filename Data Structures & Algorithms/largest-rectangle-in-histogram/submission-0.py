class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                left[i] = stack[-1]

            stack.append(i)

        stack = []
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                right[i] = stack[-1]

            stack.append(i)

        area = 0 
        for i in range(len(heights)):
            left[i]+=1
            right[i]-=1
            curr_area = heights[i] * (right[i] - left[i] + 1)
            area = max(curr_area, area)

        return area    

