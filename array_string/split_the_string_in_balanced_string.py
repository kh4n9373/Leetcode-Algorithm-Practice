class Solution:
    def balancedStringSplit(self, s) -> int:
        count = {'R':0,'L':0}
        res = 0
        for i in s:
            count[i] += 1
            if count['R'] == count['L']:
                res += 1
        return res