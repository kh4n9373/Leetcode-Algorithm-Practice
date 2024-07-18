class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        '''
        l, r, res, cur = 0, k-1, 0, 0
        Vowels = set('aeiou')

        for i in range(l, r+1):
            if s[i] in Vowels:
                cur += 1
  
        while r < len(s):
            res = max(res, cur)
            if r + 1 < len(s):
                if s[l] in Vowels:
                    cur -= 1
                if s[r+1] in Vowels:
                    cur += 1
            l += 1
            r += 1
        
        return res
        '''
        #optimize:
        vowels = set('aeiou')
        cur = sum(1 for i in range(k) if s[i] in vowels)
        res = cur
        
        for i in range(k, len(s)):
            cur += (s[i] in vowels) - (s[i-k] in vowels)
            res = max(res, cur)
            
        return res
