class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack:
                if temperatures[stack[len(stack) - 1]] >= temperatures[i]:
                    break
                index = stack.pop()    
                result[index] = i - index
            stack.append(i)        
        
        return result
