class Solution:
    def divisorGame(self, n: int) -> bool:
        hashmap = {}
        def dfs(n,record=0):
            if n <= 1:
                return record
            if n in hashmap:
                return hashmap[n]
            for i in range(1,n):
                if n%i == 0:
                    hashmap[n] = dfs(n-i,1-record)
            return hashmap[n]
        return dfs(n)