class Solution:
    def subsetXORSum(self, nums):
        res = 0
        s1 = 0

        def backtrack(i):
            nonlocal s1
            nonlocal res
            if i == len(nums):
               s2 = s1
        
               res += s2
               return 
            s1 = s1^nums[i]
            backtrack(i+1)

            s1 = s1^nums[i]
            backtrack(i+1)
        
        backtrack(0)
        return res