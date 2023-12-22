class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                skipI, skipJ = s[i+1:j+1], s[i:j]
                return ((skipI == skipI[::-1]) or skipJ == skipJ[::-1])
            i,j = i+1, j-1
        return True
            