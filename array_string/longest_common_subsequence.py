class Solution:
    def longestCommonSubsequence(self, a1: str, a2: str) -> int:
        n1,n2 = len(a1),len(a2)
        dp = [[0 for i in range(n2+1)] for j in range(n1+1)]
        for i in range(n1-1,-1,-1):
            for j in range(n2-1,-1,-1):
                if a1[i] == a2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]