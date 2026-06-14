class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left<=right:
            mid = (left+right)//2
            # Determine which half is sorted
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # Left half [left, mid] is sorted
                # Check if target lies in [nums[left], nums[mid])
                if nums[left]<=target<nums[mid]:
                    right = mid-1   # search left
                else:
                    left = mid+1  # search right
            else:
                # Right half [mid, right] is sorted
                # Check if target lies in (nums[mid], nums[right]]
                if nums[mid]<target<=nums[right]:
                    left = mid+1  # search right
                else:
                    right = mid-1   # search left
        
        return -1

        