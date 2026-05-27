from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)          # frequency of each char in the current window
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(count.values())
            # window size = right - left +1
            while (right-left+1) - max_freq >k:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len, (right-left+1))
        
        return max_len       