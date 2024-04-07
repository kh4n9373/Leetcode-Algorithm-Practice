class Solution:
    def checkValidString(self, s: str) -> bool:
        # previous solution, didnt pass all test cases 
        # stack = []
        # sub = 0
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         stack.append(s[i])
        #     elif s[i] == ')':
        #         if stack:
        #             stack.pop()
        #         else:
        #             if sub > 0:
        #                 sub -= 1
        #             else:
        #                 return False
        #     elif s[i] == '*':
        #         sub += 1
        # if len(stack) > sub:
        #     return False
        # return True
        leftMin, leftMax = 0, 0 
        for i in range(len(s)):
            if s[i] == '(':
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif s[i] == ')':
                leftMin, leftMax = leftMin - 1, leftMax - 1
            elif s[i] == '*':
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0
        
