class Solution:
    def differenceOfSum(self, nums):
        e_sum = 0
        d_sum = 0
        def cal(num):
            return sum(int(i) for i in str(num))
        for n in nums:
            e_sum += n
            if n >= 10:
                d_sum += cal(n)
            else:
                d_sum += n
        return abs(e_sum-d_sum)

