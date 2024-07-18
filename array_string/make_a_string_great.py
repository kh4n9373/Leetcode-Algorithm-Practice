
def makeGood(s):

    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            can = stack.pop()
            if s[i] == can or s[i] != can.upper() and can != s[i].upper():
                stack.append(can)
                stack.append(s[i])

    return ''.join(i for i in stack)