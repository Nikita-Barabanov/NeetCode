from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack, op = list(), {"*": lambda x, y: x * y,
                             "+": lambda x, y: x + y,
                             "/": lambda x, y: int(x / y),
                             "-": lambda x, y: x - y}
        for token in tokens:
            if token in ["*", "+", "/", "-"]:
                y, x = stack.pop(), stack.pop()
                stack.append(op[token](x, y))
            else:
                stack.append(int(token))

        return stack.pop()
