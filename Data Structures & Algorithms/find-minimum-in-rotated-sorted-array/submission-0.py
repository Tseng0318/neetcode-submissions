class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left<right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid+1     # minimum is to the right of mid
            else:
                right = mid     # minimum is at mid or before
        
        return nums[right]