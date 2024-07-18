class Solution:
    def restoreString(self, s: str, indices) -> str:
        res = [0]*len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return ''.join(str(i) for i in res)