class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty = set()
        for num in nums:
            if num in empty:
                return True
            empty.add(num)
        return False

        