import math
class Solution:
    def generate(self, numRows: int,res=[]):
        def C(i,n):
            return int(math.factorial(n)/(math.factorial(n-i)*math.factorial(i)))
        if numRows < 1:
            new = res[::-1]
            res.clear()
            return new
        res.append(list(C(i,numRows-1) for i in range(numRows)))
        return self.generate(numRows-1)
        