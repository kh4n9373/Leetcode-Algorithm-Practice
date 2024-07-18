class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        p1, p2 = 0, 0
        while p1 < len(haystack):
            memo = p1
            while p1 < len(haystack) and p2 < len(needle) and haystack[p1] == needle[p2]:
                p1 += 1
                p2 += 1
            if p2 == len(needle): return memo
            p1 = memo + 1
            p2 = 0
        return -1