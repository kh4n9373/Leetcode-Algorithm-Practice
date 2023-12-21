class Solution:
    def addDigits(self, num):
        def sumOfDigit(num):
            string,res = str(num),0 
            for i in range(len(string)):
                res += int(string[i])
            return res
        prev = sumOfDigit(num)
        if prev < 10 :
            return prev
        return self.addDigits(prev)