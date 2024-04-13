
def largestRectangleArea(heights):
    stack = []
    maxH = 0
    for index, height in enumerate(heights):
        start = index
        while stack and stack[-1][1] > height:
            start = stack[-1][0]
            maxH = max(maxH, (index-stack[-1][0])*stack[-1][1])
            stack.pop()
        stack.append((start,height))
    for i,h in stack:
        maxH = max(maxH, h*(len(heights)-i))
    return maxH