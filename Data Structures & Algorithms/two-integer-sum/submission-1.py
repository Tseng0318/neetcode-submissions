class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        empty = {}
        for i, j in enumerate(nums):
            residual = target - j
            if residual in empty:
                return [empty[residual], i]
            empty[nums[i]] = i
        