from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        result = []

        for num in nums:
            count[num] += 1

        for _ in range(k):
            top = max(count, key=count.get)
            result.append(top)
            del count[top]
        
        return result

        