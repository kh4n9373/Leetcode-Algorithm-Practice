class Solution:
    def minimumSum(self, num):
        digit = [d for d in str(num)]
        digit.sort(key=lambda x:int(x))
        digit.append('')
        first = ''
        second = ''
        
        for i in range(0,len(digit)-1,2):
            first += digit[i]
            second += digit[i+1]

        return (int(first)+int(second))