class Solution:
    def stoneGame(self, piles):
        hashmap = {}

        def dfs(l,r):
            if l > r:
                return 0
            if (l,r) in hashmap:
                return hashmap[(l,r)]
            hashmap[(l,r)] =  max(dfs(l+2,r)+piles[l],dfs(l,r-2)+piles[r])
            return hashmap[(l,r)]
        return dfs(0,len(piles)-1) > sum(piles)//2