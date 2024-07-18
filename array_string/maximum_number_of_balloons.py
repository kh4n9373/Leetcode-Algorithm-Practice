from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        res = float('inf')
        bal = {'b':1, 'a':1,'l':2,'o':2,'n':1}
        dic = defaultdict(int)
        for n in text:
            dic[n] += 1
        for n in bal:
            if bal[n] > dic[n] :
                return 0
            if n == 'l' or n == 'o': 
                bal[n] = dic[n]//2
            else: bal[n] = dic[n]
        res = min(bal.values())
        return res