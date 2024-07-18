class Solution:
    def lengthOfLastWord(self, s): 
        res = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ':
                continue
            else:
                for j in range(i,-1,-1):
                    if s[j] != ' ':
                        res += 1
                    else:
                        break
                break
        return res
                

        