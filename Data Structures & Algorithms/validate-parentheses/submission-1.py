class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}    # closer -> matching opener
        # "([{}])"
        for c in s:
            if c in mapping:
                if not stack:
                    return False
                popped = stack.pop()
                if popped != mapping[c]:
                    return False
            else:
                stack.append(c)
        
        return not stack

                