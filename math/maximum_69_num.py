class Solution:
    def maximum69Number (self, num):
        n = str(num)
        for i in range(len(n)):
            if n[i] == '6':
                n = n[:i] + '9' + n[i+1:]
                break
        return int(n)