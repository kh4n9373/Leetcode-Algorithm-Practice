class Solution:
    def stoneGameIII(self, stoneValue) -> str:
        hashmap = {}
        def dfs(i):
            if i == len(stoneValue):
                return 0
            if i in hashmap:
                return hashmap[i]
            res = float('-inf')
            for j in range(i,min(i+3,len(stoneValue))):
                res = max(res,sum(stoneValue[i:j+1])-dfs(j+1))
            hashmap[i] = res
            return hashmap[i]
        return 'Alice' if dfs(0) > 0 else('Bob' if dfs(0) <0 else 'Tie')
