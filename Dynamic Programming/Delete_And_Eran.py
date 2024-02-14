nums = [2,2,3,3,3,4]

dic = {s:0 for s in set(nums)}
cons = list(dic.keys())
cons.sort()
for n in nums:
    dic[n] += 1

dp = [0] + [dic[cons[0]]*cons[0]] + [0]*(len(dic.items())-1)
for i in range(2,len(dp)):
    if cons[i-2] != cons[i-1]-1:
        dp[i] = dp[i-1] + dic[cons[i-1]]*cons[i-1]
    elif cons[i-2] == cons[i-1]-1:
        dp[i] = max(dp[i-2] + dic[cons[i-1]]*cons[i-1],dp[i-1])

print(dp)

