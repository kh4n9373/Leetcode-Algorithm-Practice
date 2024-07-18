class Solution:
    def isValid(self, s: str) -> bool:
        l,r = {'{':0,'[':1,'(':2},{'}':0,']':1,')':2}
        stack = []
        for i in s:
            if i in l:
                stack.append(i)
            else:
                if not stack:
                    return False
                oppo = stack.pop()
                if r[i] == l[oppo]:
                    continue
                else:
                    return False
        if stack:
            return False
        return True

