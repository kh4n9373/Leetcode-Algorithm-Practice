class Solution:
    def fib(self, n: int) -> int:
        # prev
        # dp = [0,1] + [0]*(max(0,n-1))
        # for i in range(2,len(dp)):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]
        # after learning discrete math
        a = (1 + 5**0.5) / 2
        b = (1 - 5**0.5) / 2
        return round((1 / 5**0.5) * (a**n - b**n))
