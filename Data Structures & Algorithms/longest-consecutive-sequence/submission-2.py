class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        
        nums = sorted(set(nums))
        max_length = 0
        for num in nums:
            if num - 1 not in nums:
                current_num = num
                current_length = 0
                while current_num in nums:
                    current_num += 1
                    current_length += 1
            max_length = max(max_length, current_length)
        return max_length

