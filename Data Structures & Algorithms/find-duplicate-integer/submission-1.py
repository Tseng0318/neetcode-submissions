class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: cycle detection with fast/slow
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Phase 2: find cycle entry (the duplicate)
        slow2 = nums[0]
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow