class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            # 1. while s[right] is already in char_set:
            # remove s[left] from char_set
            # left += 1
            # 2. add s[right] to char_set
            # 3. update max_len with the current window length (right - left + 1)
        
        char_set = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len       