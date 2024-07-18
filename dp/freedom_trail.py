def findRotateSteps(ring: str, key: str) -> int:
    # dp 
    dp = [0] * len(ring)
    for j in range(len(key)-1,-1,-1):
        extra_dp = [float('inf')]*len(ring)
        for i in range(len(ring)):
            for k,v in enumerate(ring):
                if v == key[j]:
                    mindist = min(abs(i-k),len(ring)-abs(i-k))
                    extra_dp[i] = min(extra_dp[i],mindist + 1 + dp[k])
        dp = extra_dp
    return dp[0]

    # recursive using cache
    # n = len(ring)
    # cache = {}
    # def helper(i,j):
    #     if j == len(key):
    #         return 0 
    #     if (i,j) in cache:
    #         return cache[(i,j)]
        
    #     res = float('inf')
    #     for k,v in enumerate(ring):
    #         if v == key[j]:
    #             mindist = min(abs(i-k),n-abs(i-k))
    #             res = min(res,mindist + 1 + helper(k,j+1))
    #     cache[(i,j)] = res
    #     return res
    # return helper(0,0)
    