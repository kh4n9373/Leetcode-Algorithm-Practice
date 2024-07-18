class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # countS = {}
        # countT = {}
        # s1, t1 = list(s), list(t)
        # for i in range(len(s)):
        #     countS[s1[i]] = 1 + countS.get(s1[i], 0)
        #     countT[t1[i]] = 1 + countT.get(t1[i], 0)
        # for a in countS : 
        #     if countS[a] == countT.get(a,0):
        #         continue
        #     else:
        #         return False
        # return True
        return sorted(s) == sorted(t)

        