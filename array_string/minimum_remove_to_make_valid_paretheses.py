
def minRemoveToMakeValid(self, s: str) -> str:
    a = list(s)
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            if not stack :
                a[i] = ''
            else:
                stack.pop()
    remain = len(stack)
    count = 0
    for j in range(len(s)-1, -1,-1):
        if count == remain:
            break
        if a[j] == '(':
            a[j] = ''
            count += 1
    return ''.join(i for i in a)

