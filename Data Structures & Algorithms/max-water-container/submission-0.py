class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_area = 0
        while left<right:
            distance = right-left
            current_area = min(heights[left], heights[right]) * distance
            max_area = max(max_area, current_area)
            if heights[left] > heights[right]:
                right-=1
            else:
                left+=1

        return max_area
        