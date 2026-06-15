from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        # Find the largest stored timestamp <= timestamp; return its value, or ""
        if key not in self.store:
            return ""
        
        pairs = self.store[key]
        value = ""
        left, right = 0, len(pairs) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if pairs[mid][0] <= timestamp:
                value =  pairs[mid][1]    # remember this value, search for larger valid ts
                left = mid + 1
            else:
                right =  mid - 1    # mid ts too big, search smaller
        return value
# self.store = {"foo": [(1, "bar"), (4, "bar2"), (7, "bar3")]}