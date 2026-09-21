class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for token in tokens:
            if token in operators:
                if len(stack) >= 2:
                    result = 0
                    a = int(stack.pop())
                    b = int(stack.pop())
                    if token == operators[0]: result = b + a
                    if token == operators[1]: result = b - a
                    if token == operators[2]: result = b * a
                    if token == operators[3] and b != 0: 
                        result = b / a
                    stack.append(result)
            else:
                stack.append(token)
        return int(stack[-1])
            
    