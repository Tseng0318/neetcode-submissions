class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        result = []

        for num in nums: 
            counts[num] = counts.get(num, 0) + 1

        for _ in range(k):
            top_k = max(counts, key=counts.get)
            result.append(top_k)
            del counts[top_k]


        return result


        