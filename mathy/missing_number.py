class Solution:
    def missingNumber(self, nums):
        s = 0
        for i in range(0,len(nums)+1):
            s += i
        return s - sum(nums)