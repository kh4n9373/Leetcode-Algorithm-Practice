def maxDepth(s):
    depth = 0
    res = 0
    for i in range(len(s)):
        if s[i] == '(':
            depth += 1
            res = max(res, depth)
        elif s[i] == ')':
            depth -= 1
        
    return res