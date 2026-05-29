from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        t_count = Counter(t)

        best_len = float('inf')
        left, best_left = 0, 0
        need = len(t_count)
        have = 0
        window_count = Counter()

        for right in range(len(s)):
            c = s[right]
            window_count[c] += 1

            if c in t_count and window_count[c] == t_count[c]:
                have += 1

            while need == have:
                window = right -left + 1

                if window < best_len:
                    best_len = window
                    best_left = left
                
                left_c = s[left]
                window_count[left_c] -= 1
                if left_c in t_count and window_count[left_c] < t_count[left_c]:
                    have-=1

                left+=1

        
        if best_len == float('inf'):
            return ""
        return s[best_left : best_left + best_len]