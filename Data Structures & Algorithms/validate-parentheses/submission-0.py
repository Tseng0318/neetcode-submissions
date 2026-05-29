class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}    # closer -> matching opener
        
        for c in s:
            if c in mapping:
                # c is a closer
                # 1. if stack is empty → return False (no opener to match)
                if not stack:
                    return False
            # 2. pop the top of stack
                popped = stack.pop()
                if popped != mapping[c]:
                    return False
                # 3. if popped != mapping[c] → return False
            else:
                # c is an opener → push it
                stack.append(c)
        
        # After the loop, stack should be empty
        # return whether stack is empty
        return not stack       