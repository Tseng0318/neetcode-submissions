class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}    # set for O(1) lookup
        
        for token in tokens:
            if token in operators:
                # pop two operands (right first, then left)
                right = stack.pop()         
                left = stack.pop()                
                # compute the result based on the operator
                if token == "+":
                    result = left + right
                elif token == "-":
                    result = left - right
                elif token == "*":
                    result = left * right
                else:  # "/"
                    result = int(left / right)  
                stack.append(result)
                # push the result back
            else:
                # token is a number — convert to int and push
                stack.append(int(token))
        
        # return the only thing left on the stack
        return stack[0]