class Solution:
    def findDuplicates(self, nums):
        # Damn I'm so smart
        res = []
        
        for n in nums:
            check = abs(n)
            if nums[check-1] < 0:
                res.append(check)
            nums[check-1] = -nums[check-1]

        return res