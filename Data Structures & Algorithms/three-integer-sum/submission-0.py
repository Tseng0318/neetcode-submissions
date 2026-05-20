class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        # [-4, -1, -1, 0, 1, 2]
        for i in range(len(nums)):
            # skip duplicate fixed elements
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[left] + nums[right] + nums[i]          
                
                if total == 0:
                    # 1. record the triplet [nums[i], nums[left], nums[right]]
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # 2. move both pointers inward
                    # 3. skip duplicate values at left and right (scaffolding below)
                    
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif total < 0:
                    left += 1                        # which pointer moves, and how?
                else:
                    right -= 1                        # which pointer moves, and how?
        
        return result