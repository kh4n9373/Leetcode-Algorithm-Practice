def longestIdealString(s: str, k: int) -> int:
    # My poor dp solution 
    # def find(i):
    #     lis = []
    #     for j in range(i-1,-1,-1):
    #         if abs(ord(s[i]) - ord(s[j])) <= k:
    #             lis.append(j)
    #     return lis
    # n = len(s)
    # dp = [0] * n  
    # res = 0
    # for i in range(1, n):
    #     for j in find(i):
    #         dp[i] = max(dp[i], dp[j] + 1)
    #         res = max(dp[i],res)
    # return res + 1

    # better dp solution, capturing the previous value, 
    # dp = [0]*26
    # for c in s:
    #     cur = ord(c) - ord('a')
    #     longest = 1
    #     for scope in range(26):
    #         if abs(cur-scope) <= k:
    #             longest = max(longest,1 + dp[scope])
    #     dp[cur] = longest 
    # return max(dp)

    # O(n) time O(128) space
    dp = [0] * 128
    for c in s:
        i = ord(c)
        dp[i] = max(dp[i - k : i + k + 1]) + 1
    return max(dp)