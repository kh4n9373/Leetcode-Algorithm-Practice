class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:     
        l = len(nums)
        while val in nums:
            nums.remove(val)
            l-=1
        return l