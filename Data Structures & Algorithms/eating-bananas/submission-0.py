import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left<right:
            mid = (left + right) // 2
            
            # compute hours needed at speed `mid`
            hours = sum(math.ceil(x/mid) for x in piles)
            
            if hours <= h:
                # mid is fast enough — try smaller
                right = mid
            else:
                # mid is too slow — need bigger
                left = mid+1
        
        return left
  