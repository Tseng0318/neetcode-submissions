from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # Build s1_count
        s1_count = defaultdict(int)
        for c in s1:
            s1_count[c] += 1
        
        window_count = defaultdict(int)
        for right in range(len(s2)):
            # PHASE 1 (always): add the new right character
            window_count[s2[right]] += 1
            
            # PHASE 2 (only if window is too big): remove the leftmost
            if right >= len(s1):
                old_char = s2[right - len(s1)]
                window_count[old_char] -= 1
                if window_count[old_char] == 0:
                    del window_count[old_char]

            # PHASE 3 (only if window is now the right size): check
            if right >= len(s1) - 1:
                if window_count == s1_count:
                    return True
        
        return False