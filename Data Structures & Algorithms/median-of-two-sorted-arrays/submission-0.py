class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = sorted(nums1+nums2)
        total = len(merge)
        if total%2 == 1:
            return float(merge[total//2])
        else:
            return (merge[total//2-1] + merge[total//2])/2
        