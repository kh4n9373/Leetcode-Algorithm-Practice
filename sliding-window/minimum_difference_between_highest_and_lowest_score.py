class Solution:
    def minimumDifference(self, nums, k: int) -> int:
        if len(nums) == 1: return 0
        nums.sort()
        l, res = 0, float('inf')
        while l + k - 1 < len(nums):
            res = min(res, nums[l+k-1]-nums[l])
            l += 1
        return res
              