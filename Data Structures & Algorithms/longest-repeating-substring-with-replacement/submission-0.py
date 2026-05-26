class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}          # frequency of each char in the current window
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # 1. add s[right] to the window: increment its count
            count[s[right]] = count.get(s[right], 0) + 1
            
            # 2. find the max frequency in the window
            max_freq = max(count.values())
            
            # 3. window length = right - left + 1

            #    replacements needed = window_length - max_freq
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            #    while replacements needed > k:  (window invalid)
            #        shrink: decrement count of s[left], left += 1
            
            # 4. update max_len with the (now valid) window length
            max_len = max(max_len, (right - left + 1))
            pass
        
        return max_len       