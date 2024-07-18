class Solution:
    def judgeCircle(self, moves: str) -> bool:
        loc = [0,0]
        dic = {'U': [1,0],'R' : [0,1],'D':[-1,0],'L':[0,-1]}
        for i in moves:
            loc = [loc[j]+dic[i][j] for j in range(len(loc))]
        if loc == [0,0]:
            return True
        return False
