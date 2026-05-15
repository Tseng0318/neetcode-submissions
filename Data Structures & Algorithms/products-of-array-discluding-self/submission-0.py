import math
class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        while i < len(nums):
            holder = nums.copy( )
            holder.pop(i)
            result.append(math.prod(holder))
            i += 1
        return result

        