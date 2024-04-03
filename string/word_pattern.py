class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''
        dic, prev = {}, 0
        lis = list(pattern)[::-1]
        s += ' '
        def dup(d):
            return len(set(d.values())) != len(d.values())
        for i in range(len(s)):
            if s[i] == ' ': 
                word = s[prev:i]
                if word not in dic:
                    dic[word] = lis.pop()
                else:
                    if not lis or dic[word] != lis.pop():
                        return False
                prev = i + 1
        if lis or dup(dic):
            return False
        return True
        '''
        word = s.split(" ") 
        if len(pattern) != len(word):
            return False
        cw = {}
        wc = {}
        for c,w in zip(pattern,word):
            if c in cw and cw[c] != w:
                return False
            if w in wc and wc[w] != c:
                return False
            cw[c] = w
            wc[w] = c
        return True


        