class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        empty = {}
        for i, j in enumerate(nums):
            diff = target-j
            if diff in empty:
                return [empty[diff], i]
            empty[nums[i]] = i