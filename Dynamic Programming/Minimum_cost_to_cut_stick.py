class Solution:
    def minCost(self, n: int, cuts) -> int:
        memo = {}
        def dfs(l,r):
            if r - l == 1: #Problably not necessary
                res = 0
            if (l,r) in memo:
                return memo[(l,r)]
            res = float('inf')
            for c in cuts:
                if l < c < r:
                    res = min(res,(r-l) + dfs(l,c) + dfs(c,r))
            memo[(l,r)] = res = 0 if res == float('inf') else res
            return memo[(l,r)]
        return dfs(0,n)