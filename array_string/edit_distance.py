class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float('inf')]*(len(word2) + 1) for i in range(len(word1)+1)]
        for i in range(len(word2) + 1):
            dp[len(word1)][i] = len(word2) - i
        for j in range(len(word1) + 1):
            dp[j][len(word2)] = len(word1) - j
        for j in range(len(word1)-1,-1,-1):
            for i in range(len(word2)-1,-1,-1):
                if word1[j] == word2[i]:
                    dp[j][i] = dp[j+1][i+1]
                else:
                    dp[j][i] = 1 + min(dp[j+1][i],dp[j][i+1],dp[j+1][i+1])
        return dp[0][0]