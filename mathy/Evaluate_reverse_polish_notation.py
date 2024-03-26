import math
class Solution:
    def evalRPN(self, tokens):
        stack = []
        for v in tokens:
            if v not in '+-/*':
                stack.append(v)
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(str(math.trunc(eval(b+v+a))))
        return int(stack[-1])