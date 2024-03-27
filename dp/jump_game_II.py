class Solution:
    def jump(self, nums) -> int:
        # previous : code ngu nhu mot con bo
        # goal, maxStart = len(nums) - 1, len(nums) - 1
        # def letscal(nums,goal,maxStart,count = 0):
        #     if maxStart == 0:
        #         return count
        #     for i in range(goal,-1,-1):
        #         if i + nums[i] >= goal:
        #             maxStart = min(maxStart,i)
        #     goal = maxStart
        #     count += 1
        #     return letscal(nums,goal,maxStart,count)
        # return letscal(nums,goal,maxStart)
        # dp sol
        n = len(nums)
        dp = [float('inf')] * n  
        dp[n - 1] = 0 

        for i in range(n - 2, -1, -1): 
            furthest_jump = min(i + nums[i], n - 1)
            for j in range(i + 1, furthest_jump + 1):
                dp[i] = min(dp[i], 1 + dp[j])

        return dp[0]

        