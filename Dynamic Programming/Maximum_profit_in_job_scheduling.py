class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:

        temp = []
        for s,e,p in zip(startTime,endTime,profit):
            temp.append((s,e,p))
        temp.sort(key = lambda x:x[1])
        startTime = [x[0] for x in temp]
        endTime = [x[1] for x in temp]
        profit = [x[2] for x in temp]
        p = {}
        for i in range(len(profit)):
            for j in range(i-1,-1,-1):
                if endTime[j] <= startTime[i]:
                    p[i] = j
                    break


        arr = [0]*(len(profit))
        for i in range(len(arr)):
            arr[i] = max(profit[i] + arr[p.get(i,-1)],arr[i-1])
        return max(arr)

        # recursive solution        
        # memo = {}
        # def opt(i):
        #     if i in memo:
        #         return memo[i]
        #     if i == -1:
        #         return 0
        #     memo[i] = max(profit[i]+opt(p.get(i,-1)),opt(i-1))
        #     return memo[i]
        # return opt(len(profit)-1)

        # dp solution



            