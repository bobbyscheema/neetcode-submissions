class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]


        for token in tokens:
            if token.isnumeric():
                stack.append(token)
            if token in operators:
                if len(stack) >= 2:
                    a = int(stack.pop())
                    b = int(stack.pop())
                    if token == operators[0]: result = a + b
                    if token == operators[1]: result = a - b
                    if token == operators[2]: result = a * b
                    if token == operators[3]: result = a / b
                    stack.append(result)
        return int(stack[-1])
            
    