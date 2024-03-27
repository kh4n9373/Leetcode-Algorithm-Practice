class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        if k <= 1: return 0
        prod = 1
        res = 0 
        left, right = 0,0
        while right < len(nums):
            prod = prod * nums[right]
            
            while prod >= k :
                prod = prod/nums[left]
                left += 1
            
            res +=  right - left + 1
            right += 1
        return res