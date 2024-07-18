class Solution:
    def maxSubarrayLength(self, nums, k: int) -> int:
        # Time : O(n), Space : O(1)
        l,r = 0,0
        res = 0
        hashmap = {}
        while r < len(nums):
            hashmap[nums[r]] = hashmap.get(nums[r],0) + 1
            if hashmap[nums[r]] > k:
                while hashmap[nums[r]] > k:
                    hashmap[nums[l]] -= 1
                    l += 1
            else:
                res = max(res, r - l + 1)
            r += 1
        return res

        
        