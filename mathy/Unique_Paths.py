# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         def doTheRightThings(m,n,memo={}):
#             key = tuple([m,n])
#             if key in memo:
#                 return memo[key]
#             if m == 1 and n == 1:
#                 return 1
#             if m == 0 or n == 0:
#                 return 0
#             res = doTheRightThings(m-1,n,memo) + doTheRightThings(m,n-1,memo)
#             memo[key] = res
#             return res
#         return doTheRightThings(m,n)
def uniquePaths(m, n):
    dp = [[0 for i in range(m+2)] for j in range(n+2)]
    dp[2][2] = 1
    for i in range(1,n+2):
        for j in range(1,m+2):
            if i != 2 or j != 2:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]
print(uniquePaths(3,7))