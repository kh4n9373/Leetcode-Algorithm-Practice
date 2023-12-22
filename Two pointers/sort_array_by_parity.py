class Solution:
    def sortArrayByParity(self, nums):
        l,r = 0, len(nums)- 1
        while l < r:
            if nums[l]%2 == 0 :
                l += 1
            else:
                nums[r],nums[l]= nums[l],nums[r]
                r -=1
        return nums