class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []   # stack of INDICES; temperatures[stack[-1]] is decreasing top→bottom
        
        for i in range(n):
            # While there's someone at the back of the line, and the new day is warmer:
            while stack and temperatures[i] > temperatures[stack[-1]]:
                popped = stack.pop()         # they leave
                answer[popped] = i - popped  # record their wait
            # New day joins the back of the line
            stack.append(i)

        return answer