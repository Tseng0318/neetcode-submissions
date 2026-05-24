class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        
        nums = set(nums)
        max_len = 0
        # nums = {1, 2, 3, 100, 200}
        for num in nums:
            if num-1 not in nums:
                current_num = num
                current_len = 0
                while current_num in nums:
                    current_num += 1
                    current_len += 1
                max_len = max(max_len, current_len)

        return max_len


