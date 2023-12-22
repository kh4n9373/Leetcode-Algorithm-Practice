class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not 0 in nums:
            return nums
        else:
            index = 0
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[index] = nums[i]
                    if index != i:nums[i] = 0
                    index += 1
        return nums