class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        re = 0
        while x > 0:
            b = x%10
            re = re*10 + b
            x = x//10
        if temp == re:
            return True
        else: return False