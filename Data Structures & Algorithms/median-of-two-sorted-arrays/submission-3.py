class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # nums1 = [1, 2], nums2 = [3, 4]
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m,n = len(nums1), len(nums2) # m=2, n=2
        total = m+n # 2
        half = (total+1)//2 # 1
        left, right = 0, m # m = 2
        
        while left<=right:
            i = (left+right)//2 # 2
            j = half-i # 1

            nums1_left = nums1[i-1] if i>0 else float('-inf') # 2
            nums1_right = nums1[i]  if i < m else float('inf') # -inf
            nums2_left = nums2[j-1] if j > 0 else float('-inf') # 3
            nums2_right = nums2[j]  if j < n else float('inf')# 4
            # left = [1] right = [2, 4]
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total %2 == 1:
                    return float(max(nums1_left, nums2_left))
                else:
                    return (max(nums1_left, nums2_left) +
                            min(nums1_right, nums2_right)) / 2
            elif nums1_left>nums2_right:
                right = i-1 # i = 1
            else:
                # Took too few from nums1 → increase i
                left = i + 1 # left = 2
        return 0.0   # unreachable for valid inputs



        