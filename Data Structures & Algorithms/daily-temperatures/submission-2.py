class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0]*len(temperatures) 
        stack = [0]
        for i, temp in enumerate(temperatures):
            if i == 0:
                continue
            while stack and temp > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i-index
            stack.append(i)
        return result