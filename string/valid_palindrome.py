class Solution:
    def isPalindrome(self, s: str) -> bool:
        ac = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        l,r = 0,len(s)-1
        s = s.lower()
        while l < r:
            if s[l] not in ac:
                l += 1
                continue
            if s[r] not in ac:
                r -= 1
                continue
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True