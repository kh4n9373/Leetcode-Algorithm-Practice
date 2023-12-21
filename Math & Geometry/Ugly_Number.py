class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        else:
            if n%2 == 0:
                return self.isUgly(n/2)
            elif n%5 == 0:
                return self.isUgly(n/5)
            elif n%3 == 0:
                return self.isUgly(n/3)
            else:
                return False