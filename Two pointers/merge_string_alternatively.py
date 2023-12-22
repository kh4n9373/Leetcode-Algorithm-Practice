class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r,text = 0,0,''
        while l < len(word1) and r < len(word2):
            text += word1[l]
            text += word2[r]
            l += 1
            r += 1
        if r < len(word2):
            text += word2[r:]
        if l < len(word1):
            text += word1[l:]
        return text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                