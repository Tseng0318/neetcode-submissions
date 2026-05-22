class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        
        # Pass 1: max_left[i] = tallest bar in height[0..i]
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])        # max of previous left-max and current bar
        
        # Pass 2: max_right[i] = tallest bar in height[i..n-1]
        max_right[n-1] = height[n-1]
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])       # max of next right-max and current bar
        
        # Pass 3: sum water at each position
        total = 0
        for i in range(n):
            total += min(max_left[i], max_right[i])-height[i]             # min(left, right) - height[i]
        
        return total        