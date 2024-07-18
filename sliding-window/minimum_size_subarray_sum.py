class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        if sum(nums) < target:
            return 0
        l,total = 0,0
        res = float('inf')
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                total -= nums[l]
                res = min(r-l+1,res)
                l += 1
        return res
            