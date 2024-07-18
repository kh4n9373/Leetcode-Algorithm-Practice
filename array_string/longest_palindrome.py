class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        top = []
        for i in s:
            hashmap[i] = 1 + hashmap.get(i,0)
        for _ in hashmap:
            if hashmap[_] % 2 != 0:
                top.append(_)
        if len(top) == 0:
            return len(s)
        return len(s) - len(top) + 1
        

