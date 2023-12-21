class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0,1] + [1]*n
        for i in range(2,n+2):
            arr[i] = arr[i-1]+arr[i-2]
        return arr[-1]