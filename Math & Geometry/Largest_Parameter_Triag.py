class Solution:
    def largestPerimeter(self, nums):
        nums.sort()
        a = len(nums)-1
        b,c = a-1,a-2
        while c >= 0:
            if nums[c] + nums[b] > nums[a]:
                return nums[c] + nums[b] + nums[a]
            else:
                a,b,c = a-1,b-1,c-1
        return 0