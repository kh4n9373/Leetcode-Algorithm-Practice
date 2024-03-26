class Solution:
    def trap(self, height) -> int:
        l = len(height)
        count = 0
        maxLeft = [height[0]]*l
        maxRight = [height[l-1]]*l
        for i in range(1,l):
            maxLeft[i] = max(maxLeft[i-1],height[i])
            maxRight[l-i-1] = max(maxRight[l-i],height[l-i-1])
        for i in range(l):
            count += max(0,min(maxLeft[i],maxRight[i]) - height[i])
        return count

