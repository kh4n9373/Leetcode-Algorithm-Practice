def maximalRectangle(matrix):
    def largestArea(arr):
        stack = []
        maxH = 0
        for index, height in enumerate(arr):
            start = index
            while stack and stack[-1][1] > height:
                start = stack[-1][0]
                maxH = max(maxH, (index-stack[-1][0])*stack[-1][1])
                stack.pop()
            stack.append((start,height))
        for i,h in stack:
            maxH = max(maxH, h*(len(arr)-i))
        return maxH
    res = 0
    hist = [0]*len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '0':
                hist[j] = 0
            else:
                hist[j] += 1
        res = max(res, largestArea(hist))
    return res