class Solution :
    def countSubarrays(self, nums, k: int) -> int:
        maxnum = max(nums)
        count = 0
        l,r = 0,0
        res = 0
        for r in range(len(nums)):
            if nums[r] == maxnum:
                count += 1
            while count == k:
                if nums[l] == maxnum:
                    count -= 1
                l += 1
            res += l 
        return res