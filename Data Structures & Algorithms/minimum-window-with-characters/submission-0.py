from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""
        
        # 1. Build t_count: how many of each char t requires
        t_count = Counter(t)
        
        need = len(t_count)
        have = 0
        window_count = Counter()
        
        best_len = float('inf')
        best_left = 0
        left = 0
        
        for right in range(len(s)):
            # 2. EXPAND: add s[right] to window_count
            c = s[right]
            window_count[c] += 1
            
            # 3. Did we just satisfy a new requirement?
            # Yes IF c is required AND window_count[c] now exactly equals t_count[c]
            if c in t_count and window_count[c] == t_count[c]:
                have += 1
            
            # 4. SHRINK while window is valid (all requirements satisfied)
            while have == need:
                # 4a. Record this window if it's the shortest so far
                window_len = right-left+1  # standard "current window length" formula
                if window_len < best_len:
                    best_len = window_len
                    best_left = left
                
                # 4b. Remove the leftmost char
                left_c = s[left]
                # decrement window_count[left_c]
                window_count[s[left]] -= 1
                
                # 4c. Did we just break a requirement?
                #     Yes IF left_c is required AND window_count[left_c] dropped below t_count[left_c]
                if left_c in t_count and window_count[left_c] < t_count[left_c]:
                    have -= 1
                
                # 4d. Advance left
                left += 1
        
        # 5. Return the best window, or "" if none found
        if best_len == float('inf'):
            return ""
        return s[best_left : best_left + best_len]