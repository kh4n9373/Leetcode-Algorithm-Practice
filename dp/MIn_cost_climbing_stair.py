class Solution:
    def minCostClimbingStairs(self, cost):
        # #Tabulation
        # n = len(cost)
        # dp = [0] * (n + 1)

        # for i in range(2, n + 1):
        #     dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        # return dp[n]
        # #The best
        # cost.append(0)
        # for i in range(len(cost)-3,-1,-1):
        #     cost[i] += min(cost[i+1],cost[i+2])
        # return min(cost[0],cost[1])
        # #Memoiz
        # hashmap = {}
        # def dfs(start):
        #     if start >= len(cost):
        #         return 0
        #     if start in hashmap:
        #         return hashmap[start]
        #     hashmap[start] = cost[start] + min(dfs(start+1),dfs(start+2))
        #     return hashmap[start]
        # return min(dfs(0),dfs(1))

        def dfs(i,memo={}):
            if i in memo:
                return memo[i]
            if i >= len(cost):
                return 0
            memo[i] = cost[i] + min(dfs(i+1,memo),dfs(i+2,memo))
            return memo[i]
        return min(dfs(0),dfs(1))



