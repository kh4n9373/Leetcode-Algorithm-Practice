class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        a = n//2
        if n == 0:
            return 1
        if n == 1:
            return x
        if n > 0:
            res = self.myPow(x,a)
            if n % 2 == 0:
                return res*res
            else:
                return x*res*res
        elif n < 0:
            return 1/self.myPow(x,abs(n))