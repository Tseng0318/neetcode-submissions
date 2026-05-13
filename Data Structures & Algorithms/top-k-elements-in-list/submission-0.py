class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        result = []
        for _ in range(k):
            top_key = max(count, key=count.get)
            result.append(top_key)
            del count[top_key]
        
        return result

        