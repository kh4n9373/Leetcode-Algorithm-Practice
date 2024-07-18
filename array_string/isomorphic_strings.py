class Solution:
    def isIsomorphic(self, s, t) -> bool:
        h1 = {}
        h2 = {}
        for i in range(len(s)):
            if t[i] in h2 or s[i] in h1:
                if h2.get(t[i],0) != s[i] or h1.get(s[i],0) != t[i]:
                    return False
            else:
                h2[t[i]] = s[i]
                h1[s[i]] = t[i]
        return True
        