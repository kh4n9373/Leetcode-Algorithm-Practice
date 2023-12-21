class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        res = 0
        div = abs(dividend)
        d = abs(divisor)
        if divisor == 1:
            return dividend
        elif dividend == -2147483648 and divisor == -1:
            return 2147483647
        elif divisor == -1:
            return -dividend
        else:
            while d <= div:
                temp = d      
                mul = 1
                while temp <= div:
                    div -= temp
                    res += mul
                    mul += mul
                    temp += temp
        if dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0:
            return res
        else:
            return -res